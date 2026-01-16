from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib import messages
from .models import Topic, Chapter, UserProgress, UserProfile
from .forms import SignUpForm, UserUpdateForm
from .utils import check_and_award_badges, get_user_completion_stats
from django.utils import timezone


def home(request):
    """Public homepage"""
    return render(request, 'learning/home.html')


def signup(request):
    """User signup view"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'learning/signup.html', {'form': form})


@login_required
def dashboard(request):
    """Main learner dashboard"""
    user_profile = request.user.profile
    topics = Topic.objects.all()
    
    # Optimization: Get all started topics in one query to avoid N+1 queries
    started_topic_ids = set(UserProgress.objects.filter(
        user=request.user,
        status__in=['in_progress', 'completed']
    ).values_list('chapter__topic_id', flat=True))

    # Calculate progress for each topic
    topic_progress = []
    for topic in topics:
        progress = topic.completion_percentage(request.user)
        is_started = topic.id in started_topic_ids

        topic_progress.append({
            'topic': topic,
            'progress': progress,
            'chapters_count': topic.chapters.count(),
            'is_started': is_started,
        })
    
    # Calculate overall progress
    total_chapters = Chapter.objects.count()
    completed_chapters = UserProgress.objects.filter(
        user=request.user,
        status='completed'
    ).count()
    
    overall_progress = int((completed_chapters / total_chapters) * 100) if total_chapters > 0 else 0
    
    context = {
        'user_profile': user_profile,
        'topic_progress': topic_progress,
        'total_xp': user_profile.xp,
        'current_level': user_profile.level,
        'overall_progress': overall_progress,
    }
    return render(request, 'learning/dashboard.html', context)


@login_required
def topic_list(request):
    """Display all topics"""
    topics = Topic.objects.all().prefetch_related('chapters')
    context = {'topics': topics}
    return render(request, 'learning/topic_list.html', context)


@login_required
def topic_detail(request, topic_id):
    """Display topic with chapters"""
    topic = get_object_or_404(Topic, pk=topic_id)
    chapters = topic.chapters.all()
    
    # Get user progress for each chapter
    user_progress_map = {}
    for chapter in chapters:
        progress, _ = UserProgress.objects.get_or_create(
            user=request.user,
            chapter=chapter
        )
        user_progress_map[chapter.id] = progress
    
    context = {
        'topic': topic,
        'chapters': chapters,
        'progress_map': user_progress_map,
        'completion_percent': topic.completion_percentage(request.user),
    }
    return render(request, 'learning/topic_detail.html', context)


@login_required
def chapter_detail(request, chapter_id):
    """Display chapter content"""
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    progress, _ = UserProgress.objects.get_or_create(
        user=request.user,
        chapter=chapter
    )
    
    # Calculate remaining time (in seconds) before completion is allowed
    remaining_seconds = 0
    if progress.status == 'in_progress' and progress.started_at:
        elapsed = (timezone.now() - progress.started_at).total_seconds()
        required_seconds = chapter.estimated_time * 60
        remaining_seconds = max(0, required_seconds - elapsed)
    
    context = {
        'chapter': chapter,
        'progress': progress,
        'topic': chapter.topic,
        'remaining_seconds': int(remaining_seconds),
    }
    return render(request, 'learning/chapter_detail.html', context)


@login_required
@require_http_methods(["POST"])
def start_chapter(request, chapter_id):
    """Mark chapter as in progress"""
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    progress, _ = UserProgress.objects.get_or_create(
        user=request.user,
        chapter=chapter
    )
    
    if progress.status == 'not_started':
        progress.status = 'in_progress'
        progress.started_at = timezone.now()
        progress.save()
    
    return redirect('chapter_detail', chapter_id=chapter_id)


@login_required
def complete_chapter(request, chapter_id):
    """Mark chapter as completed and award XP"""
    chapter = get_object_or_404(Chapter, pk=chapter_id)
    progress = get_object_or_404(
        UserProgress,
        user=request.user,
        chapter=chapter
    )
    
    # Enforce minimum time spent
    if progress.status == 'in_progress' and progress.started_at:
        elapsed = (timezone.now() - progress.started_at).total_seconds()
        required_seconds = (chapter.estimated_time * 60)/2
        if elapsed < required_seconds:
            messages.warning(request, f"You're too fast! Please spend at least {chapter.estimated_time} minutes learning this chapter.")
            return redirect('chapter_detail', chapter_id=chapter_id)

    progress.mark_completed()
    
    # Check if user earned any badges
    check_and_award_badges(request.user)
    
    return redirect('topic_detail', topic_id=chapter.topic.id)


@login_required
def profile(request):
    """User profile view"""
    user_profile = request.user.profile
    badges = request.user.badges.all()
    
    # Get detailed completion stats
    stats = get_user_completion_stats(request.user)
    
    context = {
        'user_profile': user_profile,
        'badges': badges,
        'stats': stats,
    }
    return render(request, 'learning/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    return render(request, 'learning/edit_profile.html', {'u_form': u_form})
