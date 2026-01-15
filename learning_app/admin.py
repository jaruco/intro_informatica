from django.contrib import admin
from .models import Topic, Chapter, UserProfile, UserProgress, Badge


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description', 'icon', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1
    fields = ('title', 'difficulty', 'estimated_time', 'xp_reward', 'order')


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'difficulty', 'estimated_time', 'xp_reward', 'order')
    list_filter = ('topic', 'difficulty', 'created_at')
    search_fields = ('title', 'description', 'content')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Info', {
            'fields': ('topic', 'title', 'description', 'difficulty', 'order')
        }),
        ('Content', {
            'fields': ('content',),
        }),
        ('Gamification', {
            'fields': ('estimated_time', 'xp_reward'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'xp', 'created_at')
    list_filter = ('level', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('xp', 'level', 'created_at', 'updated_at')
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Profile', {
            'fields': ('avatar', 'bio'),
        }),
        ('Gamification', {
            'fields': ('xp', 'level'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'chapter', 'status', 'completed_at')
    list_filter = ('status', 'completed_at')
    search_fields = ('user__username', 'chapter__title')
    readonly_fields = ('started_at', 'completed_at', 'xp_earned')


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('title', 'badge_type')
    list_filter = ('badge_type',)
    search_fields = ('title', 'description')
    filter_horizontal = ('users_earned',)
