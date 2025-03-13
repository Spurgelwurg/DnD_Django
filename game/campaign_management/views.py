from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Campaign, CampaignSession, CampaignCharacter
from .forms import CampaignForm, CampaignSessionForm, CampaignCharacterForm


class CampaignListView(ListView):
    model = Campaign
    template_name = 'game/campaign_management/campaign_list.html'
    context_object_name = 'campaigns'


def campaign_create(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save()
            return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)
    else:
        form = CampaignForm()

    return render(request, 'game/campaign_management/campaign_form.html', {
        'form': form
    })


def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    sessions = campaign.sessions.all().order_by('session_number')
    characters = campaign.characters.all()

    return render(request, 'game/campaign_management/campaign_detail.html', {
        'campaign': campaign,
        'sessions': sessions,
        'characters': characters
    })


def campaign_edit(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    if request.method == 'POST':
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)
    else:
        form = CampaignForm(instance=campaign)

    return render(request, 'game/campaign_management/campaign_edit.html', {
        'form': form,
        'campaign': campaign
    })


def campaign_delete(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    if request.method == 'POST':
        campaign.delete()
        return redirect('game:campaign_management:campaign_list')

    return render(request, 'game/campaign_management/campaign_delete.html', {
        'campaign': campaign
    })