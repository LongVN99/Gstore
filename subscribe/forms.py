from django import forms
from .models import SubscribeUser

class SubscribeUserSignUpForm(forms:ModelForm):
    class Meta:
        model = SubscribeUser
        fields = ['email']

        def standard_email(self):
            email = self.standard_email.get('email')

            return email 
