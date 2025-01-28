from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm

from game.models import DnDUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=DnDUser.ROLE_CHOICES)

    class Meta:
        model = DnDUser
        fields = ['username', 'email', 'role']