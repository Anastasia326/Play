from abc import ABC, abstractmethod


class BattleField(ABC):
    field = [[None for i in range(10)] for j in range(12)]

    @abstractmethod
    def make_walls(self, level_of_walls) -> str:
        pass

    @abstractmethod
    def make_objects(self) -> str:
        pass
