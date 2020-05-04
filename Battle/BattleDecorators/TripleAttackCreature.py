from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.borders import in_borders


class TripleAttackCreature(BattleUnit):
    def __init__(self, base: BattleUnit):
        self.base = base.base
        self.can_conter_attack = base.can_conter_attack
        self.conter_attack = 0

    def melee_attack(self, other_creature, this_creature_army=None,
                     other_army=None, first_attack=True):
        message_to_return = []
        if self.base.length == 1:
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

        else:
            list_of_around_creatures = [[2, 2],
                                        [2, 1],
                                        [2, 0],
                                        [2, -1],
                                        [1, -1],
                                        [0, -1],
                                        [-1, -1],
                                        [-1, 0],
                                        [-1, 1],
                                        [-1, 2],
                                        [0, 2],
                                        [1, 2],
                                        ]
            attack_coordinates = [
                other_creature.base.position_on_battle_ground[0] -
                self.base.position_on_battle_ground[0],
                other_creature.base.position_on_battle_ground[1] -
                self.base.position_on_battle_ground[1]
            ]
            now_position = list_of_around_creatures.index(attack_coordinates)
            coordinates = self.base.position_on_battle_ground
            left_coordinates = [coordinates[0] +
                                list_of_around_creatures[(now_position - 1)
                                                         % 12][0],
                                coordinates[1] +
                                list_of_around_creatures[(now_position - 1)
                                                         % 12][1]]
            right_coordinates = [coordinates[0] +
                                 list_of_around_creatures[(now_position + 1)
                                                          % 12][0],
                                 coordinates[1] +
                                 list_of_around_creatures[(now_position + 1)
                                                          % 12][1]]
        if in_borders(left_coordinates) and \
                left_coordinates in other_army.army_on_field:
            target = None
            for soldier in other_army.current_army:
                if soldier.base.position_on_battle_ground == left_coordinates:
                    target = soldier
            if target is not None:
                message_to_return += super().melee_attack(
                    target,
                    this_creature_army,
                    other_army,
                    False
                )
        if in_borders(right_coordinates) and \
                right_coordinates in other_army.army_on_field:
            target = None
            for soldier in other_army.current_army:
                if soldier.base.position_on_battle_ground == right_coordinates:
                    target = soldier

            if target is not None:
                message_to_return += super().melee_attack(
                    target,
                    this_creature_army,
                    other_army,
                    False
                )
        message_to_return += super().melee_attack(other_creature)
        return message_to_return
