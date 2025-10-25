from django import forms
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    """Contact form with honeypot spam protection."""
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        label=''
    )
    
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-primary-500 focus:ring-primary-500',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-primary-500 focus:ring-primary-500',
                'placeholder': 'your.email@example.com'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-primary-500 focus:ring-primary-500',
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'block w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-primary-500 focus:ring-primary-500',
                'rows': 5,
                'placeholder': 'Your message...'
            }),
        }
    
    def clean_honeypot(self):
        """Check honeypot field for spam."""
        honeypot = self.cleaned_data.get('honeypot')
        if honeypot:
            raise forms.ValidationError('Spam detected')
        return honeypot








