from Spells.Spell import Spell
from abc import ABC, abstractmethod


class DamageSpell(Spell, ABC):
    @abstractmethod
    def deal_damage(self) -> int:
        pass
