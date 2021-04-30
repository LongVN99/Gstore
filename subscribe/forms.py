from django import forms
from .models import SubscribeUser

class SubscribeUserSignUpForm(forms.ModelForm):
    class Meta:
        model = SubscribeUser
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_email.get('email')

        return email
