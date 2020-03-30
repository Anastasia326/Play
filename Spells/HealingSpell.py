from Spells.Spell import Spell
from abc import ABC, abstractmethod


class HealingSpell(Spell, ABC):
    @abstractmethod
    def heal(self) -> int:
        pass
