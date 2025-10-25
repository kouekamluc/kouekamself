from django.contrib import admin
from .models import SpeakingEngagement, NewsletterSubscriber, PressMention


@admin.register(SpeakingEngagement)
class SpeakingEngagementAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'location', 'event_type']
    list_filter = ['event_type', 'event_date']
    search_fields = ['title', 'location', 'description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'active', 'subscribed_at']
    list_filter = ['active', 'subscribed_at']
    search_fields = ['email']
    list_editable = ['active']
    readonly_fields = ['subscribed_at']


@admin.register(PressMention)
class PressMentionAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication', 'published_date']
    list_filter = ['published_date', 'publication']
    search_fields = ['title', 'publication', 'description']
    readonly_fields = ['created_at']