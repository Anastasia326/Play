from Battle.BattleDecorators.BattleUnit import BattleUnit
from Battle.count_damage import count_damage


class Attack_without_return(BattleUnit):
    def __init__(self, base: BattleUnit):
        self.base = base.base
        self.can_conter_attack = base.can_conter_attack
        self.conter_attack = 0

    def melee_attack(self, other_creature, this_creature_army=None,
                     other_army=None, first_attack=True):
        deeling_damage = count_damage(self.base, other_creature.base)
        message_to_return = [other_creature.get_damage(deeling_damage)]
        return message_to_return
