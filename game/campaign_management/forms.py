from django import forms
from .models import Campaign, CampaignSession, CampaignCharacter

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'start_date', 'is_active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CampaignSessionForm(forms.ModelForm):
    class Meta:
        model = CampaignSession
        fields = ['session_number', 'date', 'summary']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class CampaignCharacterForm(forms.ModelForm):
    class Meta:
        model = CampaignCharacter
        fields = ['character', 'is_player_character']