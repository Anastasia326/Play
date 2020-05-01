from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.count_damage import count_damage


class Attack_and_move_back(BattleUnit):
    def __init__(self, base: BattleUnit):
        self.base = base.base
        self.can_conter_attack = base.can_conter_attack
        self.conter_attack = 0

    def melee_attack(self, other_creature, other_army=None, first_attack=True):
        deeling_damage = count_damage(self.base, other_creature.base)
        message_to_return = [other_creature.get_damage(deeling_damage)]
        return message_to_return

    def move_and_melee_attack(self, other_creature, coordinates,
                              other_army=None):
        start_coordinates = self.base.position_on_battle_ground
        message_to_return = [str(self.base.move(coordinates))]
        message_to_return += self.melee_attack(other_creature, other_army)
        message_to_return += [self.base.move(start_coordinates)]
        return message_to_return

