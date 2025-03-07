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
    
    # Reroder the default form fields
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        keys = list(self.fields.keys())
        new_order = keys[0:1] + keys[-2:] + keys[1:-2]
        self.fields = {key: self.fields[key] for key in new_order}