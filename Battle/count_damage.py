from random import randint


def count_damage(first_creature, second_creature):
    base_damage = first_creature.min_damage + randint(
        0, first_creature.max_damage - first_creature.min_damage)
    if first_creature.attack > second_creature.protection:
        attack_defense_modifier = 1 + (first_creature.attack -
                                       second_creature.protection) * 0.05
    else:
        attack_defense_modifier = 1 / (1 + (second_creature.protection -
                                            first_creature.attack) * 0.05)
    return first_creature.count * base_damage * attack_defense_modifier


def count_min_damage(first_creature, second_creature):
    base_damage = first_creature.min_damage
    if first_creature.attack > second_creature.protection:
        attack_defense_modifier = 1 + (first_creature.attack -
                                       second_creature.protection) * 0.05
    else:
        attack_defense_modifier = 1 / (1 + (second_creature.protection -
                                            first_creature.attack) * 0.05)
    return first_creature.count * base_damage * attack_defense_modifier


def count_max_damage(first_creature, second_creature):
    base_damage = first_creature.max_damage
    if first_creature.attack > second_creature.protection:
        attack_defense_modifier = 1 + (first_creature.attack -
                                       second_creature.protection) * 0.05
    else:
        attack_defense_modifier = 1 / (1 + (second_creature.protection -
                                            first_creature.attack) * 0.05)
    return first_creature.count * base_damage * attack_defense_modifier
