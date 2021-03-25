from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Magic Name'

    }))
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField()

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
