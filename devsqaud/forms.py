from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form with styled widgets."""

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-input',
                'id': 'contact-name',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com',
                'class': 'form-input',
                'id': 'contact-email',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Tell us about your project...',
                'class': 'form-input',
                'rows': 5,
                'id': 'contact-message',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) < 10:
            raise forms.ValidationError("Please provide a more detailed message.")
        return message
