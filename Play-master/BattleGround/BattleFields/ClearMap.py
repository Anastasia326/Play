from BattleGround.CreateBattleField import BattleField


class ClearMap(BattleField):
    def make_objects(self) -> str:
        return "no objects on map"

    def make_walls(self, level_of_walls) -> str:
        return "no walls on map"
