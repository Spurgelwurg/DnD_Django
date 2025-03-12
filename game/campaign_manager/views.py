from django.shortcuts import render, redirect, get_object_or_404
from .models import Campaign, NPC, Event, Villain, Location
from .forms import CampaignForm, NPCForm, EventForm, VillainForm, LocationForm
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required


def campaign_list(request):
    campaign = Campaign.objects.all()
    if request.method == 'POST':
        campaign_id = request.POST.get('campaign_id')
        campaign = get_object_or_404(Campaign, id=campaign_id)
        campaign.delete()
        return redirect('campaign_manager:campaign_list')
    
    return render(request, 'game/campaign_manager/campaign_list.html', {'campaigns': campaigns})


def campaign_create(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaign_manager:campaign_list')
    else:
        form = CampaignForm()

    return render(request, 'game/campaign_manager/campaign_form.html', {'form': form})



def campaign_edit(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    if request.method == 'POST':
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('campaign_manager:campaign_list')
    else:
        form = CampaignForm(instance=campaign)

    return render(request, 'game/campaign_manager/campaign_form.html', {'form': form})



def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    npcs = campaign.npcs.all()
    events = campaign.events.all()
    villains = campaign.villains.all()
    locations = campaign.locations.all()
    user_characters = Character.objects.filter(user=request.user, campaign=campaign)

    return render(request, 'game/campaign_manager/campaign_detail.html', {
        'campaign': campaign,
        'npcs': npcs,
        'events': events,
        'villains': villains,
        'locations': locations,
        'user_characters': user_characters
    })



def npc_create(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    if request.method == 'POST':
        form = NPCForm(request.POST)
        if form.is_valid():
            npc = form.save(commit=False)
            npc.campaign = campaign
            npc.save()
            return redirect('campaign_manager:campaign_detail', campaign_id=campaign.id)
    else:
        form = NPCForm()

    return render(request, 'game/campaign_manager/npc_form.html', {'form': form, 'campaign': campaign})



def npc_edit(request, npc_id):
    npc = get_object_or_404(NPC, id=npc_id)

    if request.method == 'POST':
        form = NPCForm(request.POST, instance=npc)
        if form.is_valid():
            form.save()
            return redirect('campaign_manager:campaign_detail', campaign_id=npc.campaign.id)
    else:
        form = NPCForm(instance=npc)

    return render(request, 'game/campaign_manager/npc_form.html', {'form': form})



def event_create(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.campaign = campaign
            event.save()
            return redirect('campaign_manager:campaign_detail', campaign_id=campaign.id)
    else:
        form = EventForm()

    return render(request, 'game/campaign_manager/event_form.html', {'form': form, 'campaign': campaign})
