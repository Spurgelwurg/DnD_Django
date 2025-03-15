from django.db import models

from DnD_Django import settings
from game.character_management.models import Character
import uuid
from django.contrib.auth.models import User


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    join_code = models.CharField(max_length=8, unique=True, blank=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_campaigns', null=True, blank=True)
    players = models.ManyToManyField(settings.AUTH_USER_MODEL, through='CampaignPlayer', related_name='campaigns')
    max_players = models.PositiveIntegerField(default=5, help_text="Maximum number of players allowed in this campaign")

    def save(self, *args, **kwargs):
        if not self.join_code:
            # Generate a unique code on first save
            self.join_code = ''.join(str(uuid.uuid4()).split('-')[0]).upper()[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    @property
    def current_player_count(self):
        return self.players.count()
    
    @property
    def is_full(self):
        return self.current_player_count >= self.max_players
    
    @property
    def spots_remaining(self):
        return max(0, self.max_players - self.current_player_count)


class CampaignPlayer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_game_master = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'campaign')

    def __str__(self):
        return f"{self.user.username} in {self.campaign.name}"


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


class Chapter(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=1)  # To organize chapters sequentially

    class Meta:
        ordering = ['order']  # Always return chapters in proper order

    def __str__(self):
        return f"{self.campaign.name} - Chapter {self.order}: {self.title}"