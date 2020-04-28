from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.count_damage import count_damage


class DamageIncreasingWithMovement(BattleUnit):
    def move_and_melee_attack(self, other_creature, coordinates):
        message_to_return = [str(self.base.position_on_battle_ground)]
        distance = abs(self.base.position_on_battle_ground[0] - coordinates[
            0]) + abs(self.base.position_on_battle_ground[1] - coordinates[1])
        message_to_return += [str(self.base.move(coordinates))]
        deeling_damage = count_damage(self.base, other_creature) + 1.2 * \
                         distance
        message_to_return = [other_creature.get_damage(deeling_damage)]
        if other_creature.conter_attack != other_creature.can_conter_attack \
                and "is dead" not in message_to_return[0]:
            other_creature.conter_attack += 1
            message_to_return += [other_creature.melee_attack(self.base,
                                                              False)]
        return message_to_return
