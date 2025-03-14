from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Campaign, CampaignPlayer
from .forms import CampaignForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import Campaign, Chapter
from .forms import CampaignForm, ChapterForm
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def chapter_create(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    
    # Check if user is part of this campaign
    if not CampaignPlayer.objects.filter(user=request.user, campaign=campaign).exists():
        messages.error(request, "You don't have access to this campaign.")
        return redirect('game:campaign_management:campaign_list')
        
    # Check if user is game master (only GMs should create chapters)
    if not CampaignPlayer.objects.filter(user=request.user, campaign=campaign, is_game_master=True).exists():
        messages.error(request, "Only game masters can create chapters.")
        return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)

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
    
    # Check if user is part of this campaign
    if not CampaignPlayer.objects.filter(user=request.user, campaign=campaign).exists():
        messages.error(request, "You don't have access to this campaign.")
        return redirect('game:campaign_management:campaign_list')
        
    chapter = get_object_or_404(Chapter, id=chapter_id, campaign=campaign)

    return render(request, 'game/campaign_management/chapter_detail.html', {
        'campaign': campaign,
        'chapter': chapter
    })


@login_required
def chapter_edit(request, campaign_id, chapter_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    
    # Check if user is part of this campaign
    if not CampaignPlayer.objects.filter(user=request.user, campaign=campaign).exists():
        messages.error(request, "You don't have access to this campaign.")
        return redirect('game:campaign_management:campaign_list')
        
    # Check if user is game master (only GMs should edit chapters)
    if not CampaignPlayer.objects.filter(user=request.user, campaign=campaign, is_game_master=True).exists():
        messages.error(request, "Only game masters can edit chapters.")
        return redirect('game:campaign_management:chapter_detail', campaign_id=campaign.id, chapter_id=chapter_id)
        
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
    
    # Check if user is part of this campaign
    if not CampaignPlayer.objects.filter(user=request.user, campaign=campaign).exists():
        messages.error(request, "You don't have access to this campaign.")
        return redirect('game:campaign_management:campaign_list')
        
    # Check if user is game master (only GMs should delete chapters)
    if not CampaignPlayer.objects.filter(user=request.user, campaign=campaign, is_game_master=True).exists():
        messages.error(request, "Only game masters can delete chapters.")
        return redirect('game:campaign_management:chapter_detail', campaign_id=campaign.id, chapter_id=chapter_id)
        
    chapter = get_object_or_404(Chapter, id=chapter_id, campaign=campaign)

    if request.method == 'POST':
        chapter.delete()
        return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)

    return render(request, 'game/campaign_management/chapter_delete.html', {
        'campaign': campaign,
        'chapter': chapter
    })

class CampaignListView(LoginRequiredMixin, ListView):
    model = Campaign
    template_name = 'game/campaign_management/campaign_list.html'
    context_object_name = 'campaigns'
    
    def get_queryset(self):
        # Only show campaigns the current user is part of
        return Campaign.objects.filter(players=self.request.user)

@login_required
def campaign_create(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.creator = request.user
            campaign.save()
            
            # Add creator as game master
            CampaignPlayer.objects.create(
                user=request.user,
                campaign=campaign,
                is_game_master=True
            )
            return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)
    else:
        form = CampaignForm()

    return render(request, 'game/campaign_management/campaign_form.html', {
        'form': form
    })

@login_required
def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    # Check if user is part of this campaign
    try:
        player = CampaignPlayer.objects.get(user=request.user, campaign=campaign)
        is_game_master = player.is_game_master
    except CampaignPlayer.DoesNotExist:
        messages.error(request, "You don't have access to this campaign.")
        return redirect('game:campaign_management:campaign_list')

    sessions = campaign.sessions.all().order_by('session_number')
    characters = campaign.characters.all()
    players = CampaignPlayer.objects.filter(campaign=campaign)

    return render(request, 'game/campaign_management/campaign_detail.html', {
        'campaign': campaign,
        'sessions': sessions,
        'characters': characters,
        'players': players,
        'is_game_master': is_game_master
    })


@login_required
def campaign_edit(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    
    # Check if user is part of this campaign and is a game master
    try:
        player = CampaignPlayer.objects.get(user=request.user, campaign=campaign)
        if not player.is_game_master:
            messages.error(request, "Only game masters can edit campaigns.")
            return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)
    except CampaignPlayer.DoesNotExist:
        messages.error(request, "You don't have access to this campaign.")
        return redirect('game:campaign_management:campaign_list')

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


@login_required
def campaign_delete(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    
    # Check if user is part of this campaign and is a game master
    try:
        player = CampaignPlayer.objects.get(user=request.user, campaign=campaign)
        if not player.is_game_master:
            messages.error(request, "Only game masters can delete campaigns.")
            return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)
    except CampaignPlayer.DoesNotExist:
        messages.error(request, "You don't have access to this campaign.")
        return redirect('game:campaign_management:campaign_list')

    if request.method == 'POST':
        campaign.delete()
        return redirect('game:campaign_management:campaign_list')

    return render(request, 'game/campaign_management/campaign_delete.html', {
        'campaign': campaign
    })


@login_required
def campaign_join(request):
    if request.method == 'POST':
        join_code = request.POST.get('join_code')
        try:
            campaign = Campaign.objects.get(join_code=join_code)
            # Check if user is already in campaign
            if not CampaignPlayer.objects.filter(user=request.user, campaign=campaign).exists():
                # Check if campaign is full
                if campaign.is_full:
                    messages.error(request, f"Sorry, the campaign '{campaign.name}' is already full ({campaign.current_player_count}/{campaign.max_players} players)")
                    return render(request, 'game/campaign_management/campaign_join.html')
                
                CampaignPlayer.objects.create(user=request.user, campaign=campaign)
                messages.success(request, f"You've joined the campaign: {campaign.name}")
            else:
                messages.info(request, "You're already a member of this campaign")
            return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)
        except Campaign.DoesNotExist:
            messages.error(request, "Invalid join code. Please try again.")

    return render(request, 'game/campaign_management/campaign_join.html')


@login_required
def manage_players(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    # Check if user is game master
    try:
        player = CampaignPlayer.objects.get(user=request.user, campaign=campaign)
        if not player.is_game_master:
            messages.error(request, "Only the game master can manage players")
            return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)
    except CampaignPlayer.DoesNotExist:
        messages.error(request, "You don't have access to this campaign.")
        return redirect('game:campaign_management:campaign_list')

    players = CampaignPlayer.objects.filter(campaign=campaign)

    if request.method == 'POST':
        action = request.POST.get('action')
        player_id = request.POST.get('player_id')

        if action == 'remove' and player_id:
            player = get_object_or_404(CampaignPlayer, id=player_id, campaign=campaign)
            player.delete()
            messages.success(request, f"{player.user.username} has been removed from the campaign")

    return render(request, 'game/campaign_management/manage_players.html', {
        'campaign': campaign,
        'players': players
    })


@login_required
def leave_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    
    try:
        player = get_object_or_404(CampaignPlayer, user=request.user, campaign=campaign)
    except CampaignPlayer.DoesNotExist:
        messages.error(request, "You're not part of this campaign.")
        return redirect('game:campaign_management:campaign_list')

    # Don't allow the game master to leave
    if player.is_game_master:
        messages.error(request, "As the game master, you cannot leave the campaign. You must delete it instead.")
        return redirect('game:campaign_management:campaign_detail', campaign_id=campaign.id)

    if request.method == 'POST':
        player.delete()
        messages.success(request, f"You have left the campaign: {campaign.name}")
        return redirect('game:campaign_management:campaign_list')

    return render(request, 'game/campaign_management/leave_campaign.html', {
        'campaign': campaign
    })