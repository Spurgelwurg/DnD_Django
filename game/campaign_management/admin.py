from django.contrib import admin
from .models import Campaign, CampaignSession, CampaignCharacter, Chapter

admin.site.register(Campaign)
admin.site.register(CampaignSession)
admin.site.register(CampaignCharacter)
admin.site.register(Chapter)