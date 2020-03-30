from BattleGround.CreateBattleField import BattleField
from random import randint


class ClearMap(BattleField):
    def make_objects(self) -> str:
        for i in range(randint(1, 5)):
            self.field[randint(0, 9)][randint(0, 11)] = "object"
        return "some objects on map"

    def make_walls(self, level_of_walls) -> str:
        return "no walls on map"
