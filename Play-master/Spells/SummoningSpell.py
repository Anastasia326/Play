from Spells.Spell import Spell
from abc import ABC, abstractmethod


class SummoningSpell(Spell, ABC):
    @abstractmethod
    def summon(self) -> dict:
        pass
