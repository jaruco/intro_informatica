from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import markdown


class Topic(models.Model):
    """Main learning topic (e.g., 'Email Basics', 'File Management')"""
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    icon = models.ImageField(upload_to='topic_icons/', blank=True, null=True)
    order = models.PositiveIntegerField(unique=True, help_text="Display order (1, 2, 3...)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Topics'

    def __str__(self):
        return self.title

    def completion_percentage(self, user):
        """Calculate completion % for a given user"""
        chapters = self.chapters.all()
        if not chapters.exists():
            return 0
        completed = UserProgress.objects.filter(
            user=user,
            chapter__topic=self,
            status='completed'
        ).count()
        return int((completed / chapters.count()) * 100)


class Chapter(models.Model):
    """Individual lesson within a topic"""
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='chapters')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    content = models.TextField(help_text="Write content in Markdown format")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    estimated_time = models.PositiveIntegerField(default=10, help_text="Minutes")
    xp_reward = models.PositiveIntegerField(default=100, help_text="XP points for completion")
    order = models.PositiveIntegerField(help_text="Display order within topic")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['topic', 'order']
        unique_together = ['topic', 'order']
        verbose_name_plural = 'Chapters'

    def __str__(self):
        return f"{self.topic.title} → {self.title}"
    
    def get_html_content(self):
        """Convert Markdown content to HTML"""
        return markdown.markdown(self.content)
    
    def get_html_description(self):
        """Convert Markdown description to HTML (for bold formatting)"""
        return markdown.markdown(self.description)


class UserProfile(models.Model):
    """Extended user profile with gamification data"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    xp = models.PositiveIntegerField(default=0, help_text="Total XP earned")
    level = models.PositiveIntegerField(default=1)
    bio = models.TextField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f"{self.user.username} (Level {self.level})"

    def calculate_level(self):
        """Calculate level based on XP (e.g., 100 XP per level)"""
        self.level = max(1, (self.xp // 100) + 1)
        self.save(update_fields=['level', 'xp'])

    def add_xp(self, amount):
        """Award XP and update level"""
        self.xp += amount
        self.calculate_level()


class UserProgress(models.Model):
    """Track user progress through chapters"""
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='user_progress')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not_started')
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    xp_earned = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ['user', 'chapter']
        verbose_name_plural = 'User Progress'

    def __str__(self):
        return f"{self.user.username} → {self.chapter.title} ({self.status})"

    def mark_completed(self):
        """Mark chapter as completed and award XP"""
        from django.utils import timezone
        self.status = 'completed'
        self.completed_at = timezone.now()
        self.xp_earned = self.chapter.xp_reward
        self.save()
        
        # Update user profile XP
        self.user.profile.add_xp(self.xp_earned)


class Badge(models.Model):
    """Achievement badges"""
    BADGE_TYPES = [
        ('milestone', 'Milestone'),
        ('achievement', 'Achievement'),
        ('streak', 'Streak'),
    ]

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.ImageField(upload_to='badges/', blank=True, null=True)
    badge_type = models.CharField(max_length=15, choices=BADGE_TYPES)
    users_earned = models.ManyToManyField(User, blank=True, related_name='badges')

    class Meta:
        verbose_name_plural = 'Badges'

    def __str__(self):
        return self.title

    @property
    def icon_url(self):
        """Safely return the icon URL or None if no icon is set."""
        if self.icon:
            return self.icon.url
        return None


# Signal to auto-create UserProfile when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
