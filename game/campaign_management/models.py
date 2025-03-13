from django.db import models
from game.character_management.models import Character


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CampaignSession(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="sessions")
    session_number = models.IntegerField()
    date = models.DateField()
    summary = models.TextField()

    def __str__(self):
        return f"{self.campaign.name} - Session {self.session_number}"


class CampaignCharacter(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="characters")
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    is_player_character = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.character.name} in {self.campaign.name}"