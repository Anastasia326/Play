from Spells.Spell import Spell
from abc import ABC, abstractmethod


class IncreaseSpell(Spell, ABC):
    @abstractmethod
    def increase(self) -> str:
        pass
