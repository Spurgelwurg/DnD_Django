from django import forms
from .models import Character, Race, SubRace, CharacterClass
from game.campaign_manager.models import Campaign


class DiceRollForm(forms.Form):
    DICE_CHOICES = [
        ('d4', 'D4'),
        ('d6', 'D6'),
        ('d8', 'D8'),
        ('d10', 'D10'),
        ('d12', 'D12'),
        ('d20', 'D20'),
        ('d100', 'D100'),
    ]
    dice_type = forms.ChoiceField(choices=DICE_CHOICES)
    number_of_dice = forms.IntegerField(min_value=1, max_value=10, initial=1)


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race', 'character_class', 'level',
                  'strength', 'dexterity', 'constitution',
                  'intelligence', 'wisdom', 'charisma',
                  'description', 'equipment', 'inventory', 'spells']

    subrace = forms.ModelChoiceField(queryset=SubRace.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'race' in self.data:
            try:
                race_id = int(self.data.get('race'))
                self.fields['subrace'].queryset = SubRace.objects.filter(parent_race_id=race_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.race:
            self.fields['subrace'].queryset = SubRace.objects.filter(parent_race=self.instance.race)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campaign'].queryset = Campaign.objects.filter(is_public=True)  

