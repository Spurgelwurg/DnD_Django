from django.shortcuts import render, get_object_or_404, redirect
from .model import Race, CharacterClass, Character
from .forms import CharacterForm
import random


# views.py

def roll_dice():
    return sum(sorted([random.randint(1, 6) for _ in range(4)])[1:])


def character_create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)

            # Würfeln für die Basiswerte
            character.strength = roll_dice() + character.race.strength_bonus
            character.dexterity = roll_dice() + character.race.dexterity_bonus
            character.intelligence = roll_dice() + character.race.intelligence_bonus

            # Speichern des Charakters
            character.save()
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterForm()
    return render(request, 'character_create.html', {'form': form})
