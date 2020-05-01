from Spells.Spell import Spell
from abc import ABC, abstractmethod


class DecreaseSpell(Spell, ABC):
    @abstractmethod
    def decrease(self) -> str:
        pass
