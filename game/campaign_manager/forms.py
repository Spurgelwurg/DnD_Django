from django import forms
from .models import Campaign, NPC, Event, Villain, Location
from django.contrib.auth.models import User


class CampaignCreateForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'player_count', 'is_public', 'dm', 'start_date', 'is_oneshot', 'number_of_sessions']
        
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
        }        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Setze den aktuellen Benutzer als GameMaster, wenn er eine Kampagne erstellt
            self.fields['dm'].initial = self.instance.dm or self.initial.get('dm', None)


class NPCForm(forms.ModelForm):
    class Meta:
        model = NPC
        fields = ['name', 'description', 'role', 'is_active', 'campaign']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date', 'location', 'campaign']


class VillainForm(forms.ModelForm):
    class Meta:
        model = Villain
        fields = ['name', 'description', 'evil_plan', 'campaign']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description', 'is_discovered', 'campaign']
