from django.core.management.base import BaseCommand
from game.character_management.models import Race, SubRace, CharacterClass


class Command(BaseCommand):
    help = 'Populate races and classes'

    def handle(self, *args, **kwargs):
        # Add races
        dwarf = Race.objects.create(
            name="Dwarf",
            description="Dwarves were raised from the earth in the elder days by a deity of the forge.",
            ability_scores="Constitution +2",
            traits="Darkvision, Dwarven Resilience, Dwarven Toughness, Stonecunning",
            age="adult 50, lifespan 350",
            size="4-5 feet, 150lbs",
            speed="25ft",
            languages="Common, Dwarvish"
        )

        # Add subraces for dwarf
        SubRace.objects.create(name="Hill Dwarf", parent_race=dwarf)
        SubRace.objects.create(name="Mountain Dwarf", parent_race=dwarf)

        # Add classes
        CharacterClass.objects.create(
            name="Barbarian",
            description="Barbarians are mighty warriors who are powered by primal forces of the multiverse that manifest as a Rage.",
            primary_ability="Strength",
            hit_die="D12",
            saving_throws="Strength & Constitution"
        )

        CharacterClass.objects.create(
            name="Bard",
            description="Bards are expert at inspiring others, soothing hurts, disheartening foes, and creating illusions.",
            primary_ability="Charisma",
            hit_die="D8",
            saving_throws="Dexterity & Charisma"
        )

        # Add more races and classes following the same pattern

        self.stdout.write(self.style.SUCCESS('Successfully populated data'))