from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm

from game.models import DnDUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
class RegisterForm(UserCreationForm):
    class Meta:
        model = DnDUser
        fields = ['username', 'email']
    
    # Reorder the default form fields
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # Put fields in this order: username, password1, password2, email
        field_order = ['username', 'password1', 'password2', 'email']
        self.fields = {key: self.fields[key] for key in field_order if key in self.fields}