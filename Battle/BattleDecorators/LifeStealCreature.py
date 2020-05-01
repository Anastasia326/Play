from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.count_damage import count_damage


class LifeStealCreature(BattleUnit):
    def __init__(self, base: BattleUnit):
        self.base = base.base
        self.can_conter_attack = base.can_conter_attack
        self.conter_attack = 0

    def melee_attack(self, other_creature, this_creature_army=None,
                     other_army=None, first_attack=True):
        deeling_damage = count_damage(self.base, other_creature.base)
        self.base.last_creature_hp += int(deeling_damage / 2)
        self.base.add_count(self.base,
                            self.base.last_creature_hp //
                            self.base.health_points)
        self.base.last_creature_hp %= self.base.health_points
        message_to_return = [other_creature.get_damage(deeling_damage)]
        message_to_return += ["Restoring " + str(int(deeling_damage / 2)) +
                              " health points. Adding " + str(
            self.base.last_creature_hp // self.health_points) + " creatures"]
        if other_creature.conter_attack != other_creature.can_conter_attack \
                and "is dead" not in message_to_return[0] and first_attack:
            other_creature.conter_attack += 1
            message_to_return += other_creature.melee_attack(
                self,
                other_army,
                this_creature_army,
                False
            )
        return message_to_return
