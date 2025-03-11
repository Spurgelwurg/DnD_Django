from django import forms
from .models import Campaign, NPC, Event, Villain, Location


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'start_date', 'end_date']


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
