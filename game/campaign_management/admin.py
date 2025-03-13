from django.contrib import admin
from .models import Campaign, CampaignSession, CampaignCharacter

admin.site.register(Campaign)
admin.site.register(CampaignSession)
admin.site.register(CampaignCharacter)