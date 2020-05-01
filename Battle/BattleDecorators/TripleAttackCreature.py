from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.borders import in_borders


class TripleAttackCreature(BattleUnit):
    def __init__(self, base: BattleUnit):
        self.base = base.base
        self.can_conter_attack = base.can_conter_attack
        self.conter_attack = 0

    def melee_attack(self, other_creature: BattleUnit, other_army=None,
                     first_attack=True):
        message_to_return = super().melee_attack(other_creature)
        list_of_around_creatures = [[1, 0],
                                    [1, 1],
                                    [0, 1],
                                    [-1, 1],
                                    [-1, 0],
                                    [-1, -1],
                                    [0, -1],
                                    [1, -1]]
        attack_coordinates = [
            other_creature.base.position_on_battle_ground[0] -
            self.base.position_on_battle_ground[0],
            other_creature.base.position_on_battle_ground[1] -
            self.base.position_on_battle_ground[1]
        ]
        now_position = list_of_around_creatures.index(attack_coordinates)
        coordinates = self.base.position_on_battle_ground
        left_coordinates = [coordinates[0] +
                            list_of_around_creatures[(now_position - 1) % 8][
                                0],
                            coordinates[1] +
                            list_of_around_creatures[(now_position - 1) % 8][
                                1]]
        right_coordinates = [coordinates[0] +
                             list_of_around_creatures[(now_position + 1) % 8][
                                 0],
                             coordinates[1] +
                             list_of_around_creatures[(now_position + 1) % 8][
                                 1]]
        if in_borders(left_coordinates) and \
                left_coordinates in other_army.army_on_field:
            target = None
            for soldier in other_army.current_army:
                if soldier.base.position_on_battle_ground == left_coordinates:
                    target = soldier
            if target is not None:
                message_to_return += super().melee_attack(target,
                                                          None, False)
        if in_borders(right_coordinates) and \
                right_coordinates in other_army.current_army:
            target = None
            for soldier in other_army.army_on_field:
                if soldier.base.position_on_battle_ground == right_coordinates:
                    target = soldier
            if target is not None:
                message_to_return += super().melee_attack(target, None,
                                                          False)
        return message_to_return
