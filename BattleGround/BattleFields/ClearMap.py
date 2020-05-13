from BattleGround.CreateBattleField import BattleField


class ClearMap(BattleField):
    def make_objects(self) -> str:
        return "no objects on map"
