from django.db import models
class CharacterClass(models.Model):
    name = models.CharField(max_length=50)
    hit_die = models.IntegerField()
    primary_ability = models.CharField(max_length=50)

    def __str__(self):
        return self.name



# Charakterklassen
class Fighter(CharacterClass):
    name = "Krieger"
    hit_die = 10
    primary_ability = "Stärke"

class Wizard(CharacterClass):
    name = "Magier"
    hit_die = 6
    primary_ability = "Intelligenz"

class Rogue(CharacterClass):
    name = "Schurke"
    hit_die = 8
    primary_ability = "Geschicklichkeit"