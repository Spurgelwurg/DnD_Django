from django.db import models

from game.character_management.model.character_class import CharacterClass
from game.character_management.model.race import Race


class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    intelligence = models.IntegerField()

    def __str__(self):
        return self.name