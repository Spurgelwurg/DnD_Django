from django.contrib import admin
from .models import Race, SubRace, CharacterClass, Character

admin.site.register(Race)
admin.site.register(SubRace)
admin.site.register(CharacterClass)
admin.site.register(Character)