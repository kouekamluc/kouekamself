from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import ContactSubmission, Profile
from .forms import ContactForm


def home(request):
    """Home page view."""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    context = {
        'profile': profile,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page view."""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    context = {
        'profile': profile,
    }
    return render(request, 'core/about.html', context)


def contact(request):
    """Contact page view with form handling."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_submission = form.save()
            
            # Send email
            try:
                send_mail(
                    subject=f"Contact Form: {form.cleaned_data['subject']}",
                    message=f"""
Name: {form.cleaned_data['name']}
Email: {form.cleaned_data['email']}
Subject: {form.cleaned_data['subject']}

Message:
{form.cleaned_data['message']}
                    """,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again.')
            
            return render(request, 'core/contact.html', {'form': ContactForm()})
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})