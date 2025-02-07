from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views import generic

from.models import Empty

class IndexView(generic.ListView):
    model = Empty
    template_name = "game/index.html"

# def simple_view(request):
#     return HttpResponse("Hello, world!")

from django.shortcuts import render, redirect
from .forms import CampaignForm

def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaign_list')  # Redirect to a list of campaigns or another page
    else:
        form = CampaignForm()
    return render(request, 'game/create_campaign.html', {'form': form})

def create_npc(request):
    if request.method == 'POST':
        form = NPCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('npc_list')  # Redirect to a list of NPCs or another page
    else:
        form = NPCForm()
    return render(request, 'game/create_npc.html', {'form': form})

def create_enemy(request):
    if request.method == 'POST':
        form = EnemyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enemy_list')  # Redirect to a list of enemies or another page
    else:
        form = EnemyForm()
    return render(request, 'game/create_enemy.html', {'form': form})

def create_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location_list')  # Redirect to a list of locations or another page
    else:
        form = LocationForm()
    return render(request, 'game/create_location.html', {'form': form})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to a list of events or another page
    else:
        form = EventForm()
    return render(request, 'game/create_event.html', {'form': form})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        
    else:
        form = TaskForm()
    return render(request, 'game/create_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'game/task_list.html', {'tasks': tasks})