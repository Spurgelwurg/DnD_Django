from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'start_date']

class NPCForm(forms.ModelForm):
    class Meta:
        model = NPC
        fields = ['name', 'description', 'campaign']

class EnemyForm(forms.ModelForm):  
    class Meta:
        model = Enemy
        fields = ['name', 'description', 'campaign']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description', 'campaign']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'campaign']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'Campaign']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'campaign']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file','description', 'campaign']