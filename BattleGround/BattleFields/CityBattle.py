from BattleGround.CreateBattleField import BattleField


class CityBattle(BattleField):
    def make_walls(self, level_of_walls) -> str:
        self.field[0][4] = level_of_walls
        self.field[1][5] = level_of_walls
        self.field[2][5] = level_of_walls
        self.field[3][5] = level_of_walls
        self.field[4][5] = level_of_walls
        self.field[5][5] = level_of_walls
        self.field[6][5] = level_of_walls
        self.field[7][5] = level_of_walls
        self.field[8][5] = level_of_walls
        self.field[9][4] = level_of_walls
        return "Walls level " + str(level_of_walls) + " were built"

    def make_objects(self):
        return "No objects were created"
