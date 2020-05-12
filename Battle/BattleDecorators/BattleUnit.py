from random import randint

from Battle.count_damage import count_damage
from Units.unit import Unit


class BattleUnit(Unit):

    def __init__(self, base: Unit, conter_attack_counter=1):
        self.base = base
        self.can_conter_attack = conter_attack_counter
        self.conter_attack = 0

    def move(self, to) -> str:
        return self.base.move(to)

    def add_count(self, count) -> str:
        return self.base.add_count(self.base, count)

    def get_damage(self, damage) -> str:
        return self.base.get_damaged(damage)

    def wait(self) -> str:
        return self.base.wait()

    def defend(self) -> str:
        return self.base.defend()

    def melee_attack(self, other_creature, this_creature_army=None,
                     other_army=None, first_attack=True):
        deeling_damage = count_damage(self.base, other_creature.base)
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

    def move_and_melee_attack(self, other_creature, coordinates,
                              this_creature_army=None,
                              other_army=None):
        message_to_return = [str(self.base.move(coordinates))]
        message_to_return += self.melee_attack(other_creature,
                                               this_creature_army,
                                               other_army)
        return message_to_return
