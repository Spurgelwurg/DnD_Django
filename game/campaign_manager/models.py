from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    player_count = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], default=1)
    is_public = models.BooleanField(default=True)
    dm = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dungeon_master', on_delete=models.CASCADE) 
    start_date = models.DateField()
    is_oneshot = models.BooleanField(default=False)
    number_of_sessions = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class NPC(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='npcs', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    role = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Villain(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='villains', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    evil_plan = models.TextField()

    def __str__(self):
        return self.name


class Location(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='locations', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_discovered = models.BooleanField(default=False)

    def __str__(self):
        return self.name
