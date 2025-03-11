from django.contrib import admin
from .models import Campaign, NPC, Event, Villain, Location

admin.site.register(Campaign)
admin.site.register(NPC)
admin.site.register(Event)
admin.site.register(Villain)
admin.site.register(Location)
