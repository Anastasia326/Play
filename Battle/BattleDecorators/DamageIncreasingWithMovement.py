from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.count_damage import count_damage


class DamageIncreasingWithMovement(BattleUnit):
    def __init__(self, base: BattleUnit):
        self.base = base.base
        self.can_conter_attack = base.can_conter_attack
        self.conter_attack = 0

    def move_and_melee_attack(self, other_creature, coordinates,
                              this_creature_army=None,
                              other_army=None):
        distance = abs(self.base.position_on_battle_ground[0] - coordinates[
            0]) + abs(self.base.position_on_battle_ground[1] - coordinates[1])
        message_to_return = [self.base.move(coordinates)]
        deeling_damage = count_damage(self.base, other_creature.base) + 1.2 * \
                         distance
        message_to_return += [other_creature.get_damage(deeling_damage)]
        if other_creature.conter_attack != other_creature.can_conter_attack \
                and "is dead" not in message_to_return[0]:
            other_creature.conter_attack += 1
            message_to_return += other_creature.melee_attack(
                self,
                other_army,
                this_creature_army,
                False
            )
        return message_to_return
