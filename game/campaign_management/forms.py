from django import forms
from .models import Campaign, CampaignSession, CampaignCharacter, Chapter


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'start_date', 'is_active', 'max_players']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'max_players': forms.NumberInput(attrs={'min': 1, 'max': 20}),
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
        fields = ['character']

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'description', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }