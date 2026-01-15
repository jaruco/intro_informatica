from learning_app.models import UserProgress, Badge, Topic
from django.db.models import Count, Q


def check_and_award_badges(user):
    """
    Check if user has earned any badges based on their progress.
    Called after each chapter completion.
    
    Badge Types:
    1. MILESTONE: Completing an entire phase/topic
    2. ACHIEVEMENT: Hidden skills (challenge chapters)
    3. STREAK: Consecutive learning days
    """
    
    # Get all topics ordered by order field
    topics = Topic.objects.all().order_by('order')
    
    for topic in topics:
        # Check if user completed ALL chapters in this topic
        chapters_in_topic = topic.chapters.count()
        completed_chapters = UserProgress.objects.filter(
            user=user,
            chapter__topic=topic,
            status='completed'
        ).count()
        
        # If user completed all chapters in a topic, award phase badge
        if chapters_in_topic > 0 and completed_chapters == chapters_in_topic:
            award_phase_badge(user, topic)


def award_phase_badge(user, topic):
    """Award phase completion badge"""
    badge_title_map = {
        1: "🏆 Personalizador Pro",           # Phase 1
        2: "📁 Maestro de Archivos",         # Phase 2
        3: "⌨️ Velocidad de Hacker",        # Phase 3
    }
    
    badge_title = badge_title_map.get(topic.order, f"🏆 {topic.title} Master")
    
    # Check if badge exists
    badge, created = Badge.objects.get_or_create(
        title=badge_title,
        defaults={
            'description': f'Completed {topic.title}',
            'badge_type': 'milestone',
            'icon': None  # Will be set manually in admin
        }
    )
    
    # Add user to badge if not already there
    if not badge.users_earned.filter(pk=user.pk).exists():
        badge.users_earned.add(user)
        print(f"✅ Badge awarded: {badge_title} to {user.username}")


def get_user_completion_stats(user):
    """
    Get completion statistics for a user across all topics
    
    Returns:
    {
        'total_xp': 150,
        'current_level': 2,
        'total_chapters': 14,
        'completed_chapters': 4,
        'completion_percentage': 29,
        'phases_completed': ['Mi Cuartel General'],
        'phases_in_progress': ['El Archivo Maestro'],
        'phases_not_started': ['Superpoderes del Teclado'],
        'badges_earned': 1,
    }
    """
    
    total_xp = user.profile.xp
    current_level = user.profile.level
    
    # Overall chapter stats - SQLite compatible (no DISTINCT ON)
    total_chapters = UserProgress.objects.filter(user=user).values('chapter').distinct().count()
    completed_chapters = UserProgress.objects.filter(
        user=user,
        status='completed'
    ).count()
    
    completion_percentage = int(
        (completed_chapters / total_chapters * 100) if total_chapters > 0 else 0
    )
    
    # Phase completion breakdown
    phases_completed = []
    phases_in_progress = []
    phases_not_started = []
    
    for topic in Topic.objects.all().order_by('order'):
        chapters_in_topic = topic.chapters.count()
        completed_in_topic = UserProgress.objects.filter(
            user=user,
            chapter__topic=topic,
            status='completed'
        ).count()
        
        if chapters_in_topic == 0:
            continue
        
        completion_pct = (completed_in_topic / chapters_in_topic) * 100
        
        if completion_pct == 100:
            phases_completed.append(topic.title)
        elif completion_pct > 0:
            phases_in_progress.append({
                'name': topic.title,
                'progress': int(completion_pct)
            })
        else:
            phases_not_started.append(topic.title)
    
    badges_earned = user.badges.count()
    
    return {
        'total_xp': total_xp,
        'current_level': current_level,
        'total_chapters': total_chapters,
        'completed_chapters': completed_chapters,
        'completion_percentage': completion_percentage,
        'phases_completed': phases_completed,
        'phases_in_progress': phases_in_progress,
        'phases_not_started': phases_not_started,
        'badges_earned': badges_earned,
    }


def calculate_next_level_xp(current_level):
    """Calculate XP needed to reach next level (100 XP per level)"""
    xp_per_level = 100
    next_level_threshold = (current_level + 1) * xp_per_level
    return next_level_threshold


def get_leaderboard(limit=10):
    """Get top learners by XP"""
    from django.contrib.auth.models import User
    
    leaderboard = User.objects.annotate(
        total_xp=Count('profile__xp'),
        total_level=Count('profile__level')
    ).order_by('-profile__xp')[:limit]
    
    return [
        {
            'rank': idx + 1,
            'username': user.username,
            'xp': user.profile.xp,
            'level': user.profile.level,
            'badges': user.badges.count(),
        }
        for idx, user in enumerate(leaderboard)
    ]
