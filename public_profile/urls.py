from django.urls import path
from . import views

app_name = 'public_profile'

urlpatterns = [
    path('media-kit/', views.media_kit, name='media_kit'),
    path('speaking/', views.speaking_engagements, name='speaking_engagements'),
    path('press/', views.press_mentions, name='press_mentions'),
    path('newsletter-signup/', views.NewsletterSignupView.as_view(), name='newsletter_signup'),
]








