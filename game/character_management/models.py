from django.db import models
from django.conf import settings  # Import settings to access AUTH_USER_MODEL


class Race(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ability_scores = models.CharField(max_length=100)  # e.g. "Constitution +2"
    traits = models.TextField()
    age = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    speed = models.CharField(max_length=50)
    languages = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubRace(models.Model):
    name = models.CharField(max_length=100)
    parent_race = models.ForeignKey(Race, related_name='subraces', on_delete=models.CASCADE)
    additional_traits = models.TextField(blank=True)
    additional_ability_scores = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.parent_race.name})"


class CharacterClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    primary_ability = models.CharField(max_length=100)
    hit_die = models.CharField(max_length=10)
    saving_throws = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Character(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='characters', null=True)
    name = models.CharField(max_length=100)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    subrace = models.ForeignKey(SubRace, on_delete=models.SET_NULL, null=True, blank=True)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.SET_NULL, null=True)
    level = models.IntegerField(default=1)

    # Ability scores
    strength = models.IntegerField(default=0)
    dexterity = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)

    # Additional fields
    description = models.TextField(blank=True)
    equipment = models.TextField(blank=True)
    inventory = models.TextField(blank=True)
    spells = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - Level {self.level} {self.character_class} {self.race}"

    def get_ability_modifier(self, ability_score):
        return (ability_score - 10) // 2