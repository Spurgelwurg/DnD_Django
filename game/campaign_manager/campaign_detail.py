from django.shortcuts import render, get_object_or_404
from ..models import Campaign

def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    npcs = campaign.npcs.all()
    events = campaign.events.all()
    villains = campaign.villains.all()
    locations = campaign.locations.all()

    return render(request, 'campaign_manager/campaign_detail.html', {
        'campaign': campaign,
        'npcs': npcs,
        'events': events,
        'villains': villains,
        'locations': locations
    })
