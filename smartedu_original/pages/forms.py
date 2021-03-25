from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Magic Name'

    }))
    last_name = forms.CharField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Magic Surname'

    }))
    email = forms.EmailField(widget=forms.EmailInput({
        'class': 'form-control',
        'placeholder': 'Magic Email'

    }))
    phone = forms.CharField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder':  'Magic Phone'

    }))
    message = forms.CharField(widget=forms.Textarea({
        'class': 'form-control',
        'placeholder': 'Magic Message'

    }))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
