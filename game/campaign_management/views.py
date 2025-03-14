from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Campaign, CampaignSession, CampaignCharacter
from .forms import CampaignForm, CampaignSessionForm, CampaignCharacterForm

from django.contrib.auth.decorators import login_required
from .models import Campaign, CampaignSession, CampaignCharacter, Chapter
from .forms import CampaignForm, CampaignSessionForm, CampaignCharacterForm, ChapterForm


@login_required
def chapter_create(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    if request.method == 'POST':
        form = ChapterForm(request.POST)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.campaign = campaign
            chapter.save()
            return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)
    else:
        # Default to the next order number
        next_order = 1
        if campaign.chapters.exists():
            next_order = campaign.chapters.order_by('-order').first().order + 1
        form = ChapterForm(initial={'order': next_order})

    return render(request, 'game/campaign_management/chapter_form.html', {
        'form': form,
        'campaign': campaign
    })


@login_required
def chapter_detail(request, campaign_id, chapter_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    chapter = get_object_or_404(Chapter, id=chapter_id, campaign=campaign)

    return render(request, 'game/campaign_management/chapter_detail.html', {
        'campaign': campaign,
        'chapter': chapter
    })


@login_required
def chapter_edit(request, campaign_id, chapter_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    chapter = get_object_or_404(Chapter, id=chapter_id, campaign=campaign)

    if request.method == 'POST':
        form = ChapterForm(request.POST, instance=chapter)
        if form.is_valid():
            form.save()
            return redirect('game:campaign_management:chapter_detail',
                            campaign_id=campaign.id,
                            chapter_id=chapter.id)
    else:
        form = ChapterForm(instance=chapter)

    return render(request, 'game/campaign_management/chapter_edit.html', {
        'form': form,
        'campaign': campaign,
        'chapter': chapter
    })


@login_required
def chapter_delete(request, campaign_id, chapter_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    chapter = get_object_or_404(Chapter, id=chapter_id, campaign=campaign)

    if request.method == 'POST':
        chapter.delete()
        return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)

    return render(request, 'game/campaign_management/chapter_delete.html', {
        'campaign': campaign,
        'chapter': chapter
    })

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