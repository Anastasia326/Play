from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.count_damage import count_damage


class KillingOneCreature(BattleUnit):

    def melee_attack(self, other_creature, first_attack=True):
        deeling_damage = count_damage(self.base, other_creature)
        if deeling_damage < other_creature.last_creature_hp:
            deeling_damage = other_creature.last_creature_hp
        message_to_return = [other_creature.get_damage(deeling_damage)]
        if other_creature.conter_attack != other_creature.can_conter_attack \
                and "is dead" not in message_to_return[0] and first_attack:
            other_creature.conter_attack += 1
            message_to_return += [other_creature.melee_attack(self.base,
                                                              False)]
        return message_to_return
