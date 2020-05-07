from abc import ABC, abstractmethod


class BattleField(ABC):
    field = [[None for i in range(12)] for j in range(10)]

    @abstractmethod
    def make_walls(self, level_of_walls) -> str:
        pass

    @abstractmethod
    def make_objects(self) -> str:
        pass
