from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Character, Race, SubRace, CharacterClass
from .forms import CharacterForm, DiceRollForm
from .dice import roll_dice as dice_roller, roll_ability_scores as roll_scores



class CharacterListView(ListView):
    model = Character
    template_name = 'game/character_management/character_list.html'
    context_object_name = 'characters'


def character_create(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            character = form.save()
            return redirect('game:character_management:character_detail', character_id=character.id)
    else:
        form = CharacterForm()

    context = {
        'form': form,
        'dice_form': DiceRollForm(),
        'races': Race.objects.all(),
        'classes': CharacterClass.objects.all(),
    }
    return render(request, 'game/character_management/character_form.html', context)


#def character_detail(request, character_id):
#    character = get_object_or_404(Character, id=character_id)
#    return render(request, 'character_management/character_detail.html.html', {
#        'character': character,
#    })

def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    return render(request, 'game/character_management/character_detail.html', {
        'character': character,
    })


def roll_dice(request):
    if request.method == 'POST':
        form = DiceRollForm(request.POST)
        if form.is_valid():
            dice_type = form.cleaned_data['dice_type']
            number_of_dice = form.cleaned_data['number_of_dice']
            result = dice_roller(dice_type, number_of_dice)
            return render(request, 'game/character_management/dice_result.html', {'result': result})
    else:
        form = DiceRollForm()

    return render(request, 'game/character_management/dice_form.html', {'form': form})


def roll_ability_scores(request):
    scores = roll_scores()
    return render(request, 'game/character_management/ability_scores.html', {'scores': scores})


def get_subrace(request):
    race_id = request.GET.get('race_id')
    subraces = SubRace.objects.filter(parent_race_id=race_id).values('id', 'name')
    return JsonResponse(list(subraces), safe=False)


def character_edit(request, character_id):
    character = get_object_or_404(Character, id=character_id)

    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect('game:character_management:character_detail', character_id=character.id)
    else:
        form = CharacterForm(instance=character)

    return render(request, 'game/character_management/character_edit.html', {
        'form': form,
        'character': character
    })

def get_race_details(request):
    race_id = request.GET.get('race_id')
    try:
        race = Race.objects.get(id=race_id)
        data = {
            'name': race.name,
            'description': race.description,
            'ability_scores': race.ability_scores,
            'traits': race.traits,
            'age': race.age,
            'size': race.size,
            'speed': race.speed,
            'languages': race.languages,
        }
        return JsonResponse(data)
    except Race.DoesNotExist:
        return JsonResponse({'error': 'Race not found'}, status=404)

def get_class_details(request):
    class_id = request.GET.get('class_id')
    try:
        character_class = CharacterClass.objects.get(id=class_id)
        data = {
            'name': character_class.name,
            'description': character_class.description,
            'primary_ability': character_class.primary_ability,
            'hit_die': character_class.hit_die,
            'saving_throws': character_class.saving_throws,
        }
        return JsonResponse(data)
    except CharacterClass.DoesNotExist:
        return JsonResponse({'error': 'Class not found'}, status=404)


def character_delete(request, character_id):
    character = get_object_or_404(Character, id=character_id)

    if request.method == 'POST':
        character.delete()
        return redirect('game:character_management:character_list')

    return render(request, 'game/character_management/character_delete.html', {
        'character': character
    })





###─────────▄──────────────▄
###────────▌▒█───────────▄▀▒▌
###────────▌▒▒▀▄───────▄▀▒▒▒▐
###───────▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
###─────▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
###───▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀██▀▒▌
###──▐▒▒▒▄▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▒▌
###──▌▒▒▐▄█▀▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
###─▐▒▒▒▒▒▒▒▒▒▒▒▌██▀▒▒▒▒▒▒▒▒▀▄▌
###─▌▒▀▄██▄▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌
###─▌▀▐▄█▄█▌▄▒▀▒▒▒▒▒▒░░░░░░▒▒▒▐
###▐▒▀▐▀▐▀▒▒▄▄▒▄▒▒▒▒▒░░░░░░▒▒▒▒▌
###▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒░░░░░░▒▒▒▐
###─▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌
###─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐
###──▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▌
###────▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
###───▐▀▒▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
###──▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀
