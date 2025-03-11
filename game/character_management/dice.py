import random


def roll_dice(dice_type, number_of_dice=1):
    """Roll dice of a specific type a certain number of times."""
    dice_map = {
        'd4': 4,
        'd6': 6,
        'd8': 8,
        'd10': 10,
        'd12': 12,
        'd20': 20,
        'd100': 100
    }

    sides = dice_map.get(dice_type, 6)  # Default to d6 if type not found
    results = [random.randint(1, sides) for _ in range(number_of_dice)]

    return {
        'dice_type': dice_type,
        'number_of_dice': number_of_dice,
        'results': results,
        'total': sum(results)
    }


def roll_ability_scores():
    """Roll 6 ability scores (3d6 for each)."""
    scores = []
    for _ in range(6):
        roll = roll_dice('d6', 3)
        scores.append({
            'rolls': roll['results'],
            'total': roll['total']
        })
    return scores