from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    strength_bonus = models.IntegerField(default=0)
    dexterity_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# TODO(jmeusel): Werte anpassen
class Human(Race):
    name = "Mensch"
    description = "Vielseitig, anpassungsfähig und ehrgeizig."
    strength_bonus = 1
    dexterity_bonus = 1
    intelligence_bonus = 1

class Elf(Race):
    name = "Elf"
    description = "Höchst agierend, mit einer langen Lebensspanne und tiefer Weisheit."
    strength_bonus = 0
    dexterity_bonus = 2
    intelligence_bonus = 1
class Dwarf(Race):
    name = "Zwerg"
    description = "Stark, zäh und mit einer natürlichen Affinität zur Erde."
    strength_bonus = 2
    dexterity_bonus = 0
    intelligence_bonus = 0
class Halfling(Race):
    name = "Halbling"
    description = "Klein, flink und besonders geschickt."
    strength_bonus = 0
    dexterity_bonus = 2
    intelligence_bonus = 0