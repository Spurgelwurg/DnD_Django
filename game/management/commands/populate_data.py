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

        elf = Race.objects.create(
            name="Elf",
            description="Elves are a magical people of otherworldly grace, living in the world but not entirely part of it.",
            ability_scores="Dexterity +2",
            traits="Darkvision, Keen Senses, Fey Ancestry, Trance",
            age="adult 100, lifespan 750",
            size="5-6 feet, 100-150lbs",
            speed="30ft",
            languages="Common, Elvish"
        )

        halfling = Race.objects.create(
            name="Halfling",
            description="Halflings are a small race known for their resourcefulness, courage, and curiosity.",
            ability_scores="Dexterity +2",
            traits="Lucky, Brave, Halfling Nimbleness",
            age="adult 20, lifespan 150",
            size="3 feet, 40lbs",
            speed="25ft",
            languages="Common, Halfling"
        )

        human = Race.objects.create(
            name="Human",
            description="Humans are the most adaptable and ambitious people among the common races.",
            ability_scores="All Abilities +1",
            traits="Extra Language",
            age="adult 18, lifespan 80",
            size="5-6 feet, 125-250lbs",
            speed="30ft",
            languages="Common, One Additional Language"
        )

        dragonborn = Race.objects.create(
            name="Dragonborn",
            description="Born of dragons, as their name proclaims, dragonborn walk proudly through a world that greets them with fearful incomprehension.",
            ability_scores="Strength +2, Charisma +1",
            traits="Draconic Ancestry, Breath Weapon, Damage Resistance",
            age="adult 15, lifespan 80",
            size="6+ feet, 250lbs",
            speed="30ft",
            languages="Common, Draconic"
        )

        gnome = Race.objects.create(
            name="Gnome",
            description="A gnome's energy and enthusiasm for living shines through every inch of their tiny bodies.",
            ability_scores="Intelligence +2",
            traits="Darkvision, Gnome Cunning",
            age="adult 40, lifespan 350-500",
            size="3-4 feet, 40lbs",
            speed="25ft",
            languages="Common, Gnomish"
        )

        half_elf = Race.objects.create(
            name="Half-Elf",
            description="Half-elves combine what some say are the best qualities of their elf and human parents.",
            ability_scores="Charisma +2, Two Others +1",
            traits="Darkvision, Fey Ancestry, Skill Versatility",
            age="adult 20, lifespan 180",
            size="5-6 feet, 100-180lbs",
            speed="30ft",
            languages="Common, Elvish, One Additional Language"
        )

        half_orc = Race.objects.create(
            name="Half-Orc",
            description="Half-orcs' grayish pigmentation, sloping foreheads, jutting jaws, prominent teeth, and towering builds make their orcish heritage plain for all to see.",
            ability_scores="Strength +2, Constitution +1",
            traits="Darkvision, Menacing, Relentless Endurance, Savage Attacks",
            age="adult 14, lifespan 75",
            size="5-6.5 feet, 180-250lbs",
            speed="30ft",
            languages="Common, Orc"
        )

        tiefling = Race.objects.create(
            name="Tiefling",
            description="Tieflings are derived from human bloodlines, and in the broadest possible sense, they still look human.",
            ability_scores="Charisma +2, Intelligence +1",
            traits="Darkvision, Hellish Resistance, Infernal Legacy",
            age="adult 18, lifespan 100",
            size="5-6 feet, 110-180lbs",
            speed="30ft",
            languages="Common, Infernal"
        )

        # Add subraces
        SubRace.objects.create(name="Hill Dwarf", parent_race=dwarf)
        SubRace.objects.create(name="Mountain Dwarf", parent_race=dwarf)

        SubRace.objects.create(name="High Elf", parent_race=elf)
        SubRace.objects.create(name="Wood Elf", parent_race=elf)
        SubRace.objects.create(name="Dark Elf (Drow)", parent_race=elf)

        SubRace.objects.create(name="Lightfoot", parent_race=halfling)
        SubRace.objects.create(name="Stout", parent_race=halfling)

        SubRace.objects.create(name="Forest Gnome", parent_race=gnome)
        SubRace.objects.create(name="Rock Gnome", parent_race=gnome)

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

        CharacterClass.objects.create(
            name="Cleric",
            description="Clerics are intermediaries between the mortal world and the distant planes of the gods.",
            primary_ability="Wisdom",
            hit_die="D8",
            saving_throws="Wisdom & Charisma"
        )

        CharacterClass.objects.create(
            name="Druid",
            description="Druids revere nature above all, gaining their spells and other magical powers from the force of nature itself.",
            primary_ability="Wisdom",
            hit_die="D8",
            saving_throws="Intelligence & Wisdom"
        )

        CharacterClass.objects.create(
            name="Fighter",
            description="Fighters share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat.",
            primary_ability="Strength or Dexterity",
            hit_die="D10",
            saving_throws="Strength & Constitution"
        )

        CharacterClass.objects.create(
            name="Monk",
            description="Monks are united in their ability to magically harness the energy that flows in their bodies.",
            primary_ability="Dexterity & Wisdom",
            hit_die="D8",
            saving_throws="Strength & Dexterity"
        )

        CharacterClass.objects.create(
            name="Paladin",
            description="Paladins are united by their oaths to stand against the forces of evil.",
            primary_ability="Strength & Charisma",
            hit_die="D10",
            saving_throws="Wisdom & Charisma"
        )

        CharacterClass.objects.create(
            name="Ranger",
            description="Far from urban centers, rangers keep their unending watch over threats that rise from the wilderness.",
            primary_ability="Dexterity & Wisdom",
            hit_die="D10",
            saving_throws="Strength & Dexterity"
        )

        CharacterClass.objects.create(
            name="Rogue",
            description="Rogues rely on skill, stealth, and their foes' vulnerabilities to get the upper hand in any situation.",
            primary_ability="Dexterity",
            hit_die="D8",
            saving_throws="Dexterity & Intelligence"
        )

        CharacterClass.objects.create(
            name="Sorcerer",
            description="Sorcerers carry a magical birthright conferred upon them by an exotic bloodline, some otherworldly influence, or exposure to unknown cosmic forces.",
            primary_ability="Charisma",
            hit_die="D6",
            saving_throws="Constitution & Charisma"
        )

        CharacterClass.objects.create(
            name="Warlock",
            description="Warlocks are seekers of the knowledge that lies hidden in the fabric of the multiverse.",
            primary_ability="Charisma",
            hit_die="D8",
            saving_throws="Wisdom & Charisma"
        )

        CharacterClass.objects.create(
            name="Wizard",
            description="Wizards are supreme magic-users who define and shape the nature of magic itself.",
            primary_ability="Intelligence",
            hit_die="D6",
            saving_throws="Intelligence & Wisdom"
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated data'))