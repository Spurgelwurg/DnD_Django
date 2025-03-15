from django.shortcuts import redirect
from django.contrib import messages
from .models import CampaignPlayer

def check_campaign_access(view_func):
    """
    Decorator that checks if a user has access to a campaign.
    Use this on views that take campaign_id as a parameter.
    """
    def wrapped_view(request, campaign_id, *args, **kwargs):
        # Check if user is part of this campaign
        if not CampaignPlayer.objects.filter(
            user=request.user, 
            campaign_id=campaign_id
        ).exists():
            messages.error(request, "You don't have access to this campaign.")
            return redirect('game:campaign_management:campaign_list')
        return view_func(request, campaign_id, *args, **kwargs)
    return wrapped_view

def check_campaign_gm_status(view_func):
    """
    Decorator that checks if a user is the game master of a campaign.
    Use this on views that take campaign_id as a parameter and require GM privileges.
    """
    def wrapped_view(request, campaign_id, *args, **kwargs):
        # Check if user is part of this campaign and is a game master
        try:
            player = CampaignPlayer.objects.get(
                user=request.user, 
                campaign_id=campaign_id
            )
            if not player.is_game_master:
                messages.error(request, "Only game masters can perform this action.")
                return redirect('game:campaign_management:campaign_detail', campaign_id=campaign_id)
        except CampaignPlayer.DoesNotExist:
            messages.error(request, "You don't have access to this campaign.")
            return redirect('game:campaign_management:campaign_list')
        return view_func(request, campaign_id, *args, **kwargs)
    return wrapped_view

def is_campaign_member(request, campaign):
    """
    Checks if user is a member of the campaign.
    Returns True if they are, False otherwise.
    """
    return CampaignPlayer.objects.filter(
        user=request.user, 
        campaign=campaign
    ).exists()

def is_campaign_game_master(request, campaign):
    """
    Checks if user is a game master of the campaign.
    Returns True if they are, False otherwise.
    """
    return CampaignPlayer.objects.filter(
        user=request.user, 
        campaign=campaign,
        is_game_master=True
    ).exists()
