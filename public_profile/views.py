from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views import View
from .models import SpeakingEngagement, PressMention, NewsletterSubscriber


def media_kit(request):
    """Media kit page with downloadable assets."""
    return render(request, 'public_profile/media_kit.html')


def speaking_engagements(request):
    """List of speaking engagements."""
    engagements = SpeakingEngagement.objects.all()
    
    context = {
        'engagements': engagements,
    }
    return render(request, 'public_profile/speaking_engagements.html', context)


def press_mentions(request):
    """List of press mentions."""
    mentions = PressMention.objects.all()
    
    context = {
        'mentions': mentions,
    }
    return render(request, 'public_profile/press_mentions.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class NewsletterSignupView(View):
    """Newsletter signup view."""
    
    def post(self, request):
        email = request.POST.get('email')
        
        if not email:
            return JsonResponse({'success': False, 'message': 'Email is required'})
        
        try:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(
                email=email,
                defaults={'active': True}
            )
            
            if created:
                return JsonResponse({
                    'success': True, 
                    'message': 'Successfully subscribed to newsletter!'
                })
            else:
                return JsonResponse({
                    'success': False, 
                    'message': 'Email already subscribed'
                })
        except Exception as e:
            return JsonResponse({
                'success': False, 
                'message': 'An error occurred. Please try again.'
            })