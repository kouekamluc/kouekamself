from django.db import models
from django.utils.text import slugify


class SpeakingEngagement(models.Model):
    """Model for speaking engagements and events."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    event_date = models.DateField()
    location = models.CharField(max_length=200)
    event_type = models.CharField(
        max_length=50,
        choices=[
            ('conference', 'Conference'),
            ('meetup', 'Meetup'),
            ('workshop', 'Workshop'),
            ('webinar', 'Webinar'),
            ('podcast', 'Podcast'),
            ('interview', 'Interview'),
        ],
        default='conference'
    )
    slides_url = models.URLField(blank=True)
    video_url = models.URLField(blank=True)
    event_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-event_date']
        verbose_name = "Speaking Engagement"
        verbose_name_plural = "Speaking Engagements"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} - {self.location}"


class NewsletterSubscriber(models.Model):
    """Model for newsletter subscribers."""
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-subscribed_at']
        verbose_name = "Newsletter Subscriber"
        verbose_name_plural = "Newsletter Subscribers"
    
    def __str__(self):
        return self.email


class PressMention(models.Model):
    """Model for press mentions and media coverage."""
    title = models.CharField(max_length=200)
    publication = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    published_date = models.DateField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-published_date']
        verbose_name = "Press Mention"
        verbose_name_plural = "Press Mentions"
    
    def __str__(self):
        return f"{self.title} - {self.publication}"