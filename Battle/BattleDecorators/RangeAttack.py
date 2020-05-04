from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.count_damage import count_damage


class RangeAttackCreature(BattleUnit):
    def __init__(self, base: BattleUnit):
        self.base = base.base
        self.can_conter_attack = base.can_conter_attack
        self.conter_attack = 0

    def melee_attack(self, other_creature, this_creature_army=None,
                     other_army=None, first_attack=True):
        deeling_damage = count_damage(self.base, other_creature.base) / 2
        message_to_return = [other_creature.get_damage(deeling_damage)]
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

    def range_attack(self, other_creature, other_army=None,
                     first_attack=True, modificator=1):
        deeling_damage = modificator * count_damage(self.base,
                                                    other_creature.base)
        self.base.shots -= 1
        if abs(self.base.position_on_battle_ground[0] -
               other_creature.base.position_on_battle_ground[0]) + \
                abs(self.base.position_on_battle_ground[1] -
                    other_creature.base.position_on_battle_ground[1]) > 8:
            deeling_damage /= 2
        message_to_return = [other_creature.get_damage(deeling_damage)]
        if "Hunter" in self.base.name and \
                "is dead" not in message_to_return[0]:
            message_to_return += [other_creature.get_damage(deeling_damage)]
        if other_creature.conter_attack != other_creature.can_conter_attack \
                and "is dead" not in message_to_return[0] and first_attack \
                and hasattr(other_creature, "range_attack") and \
                other_creature.base.shots > 0:
            other_creature.conter_attack += 1
            message_to_return += [other_creature.range_attack(self,
                                                              None,
                                                              False)]
        return message_to_return
