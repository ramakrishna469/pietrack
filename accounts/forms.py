import re
from django import forms
from piebase.models import User

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    organization = forms.CharField()
    class Meta:
        model = User
        fields = ['email', 'first_name', 'password', 'username']

