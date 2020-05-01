from Map.MapBuilder import MapBuilder
from random import randint


class QuickMap(MapBuilder):
    def __init__(self, class_first, class_second):
        super().__init__(50, 10, class_first, class_second)

    def add_cities(self, class_first, class_second):
        return None

    def add_miners(self):
        return None

    def place_heroes(self, first_hero, second_hero):
        self.Map[5][5] = first_hero
        self.Map[44][5] = second_hero

    def add_buildings(self):
        self.Map[5][1] = "Camp"
        self.Map[44][9] = "Camp"
        self.Map[1][5] = "MagicStone"
        self.Map[44][1] = "MagicStone"
        self.Map[5][9] = "DefenseBuilding"
        self.Map[45][5] = "DefenseBuilding"
        self.Map[5][6] = "WitchCraftStone"
        self.Map[44][6] = "WitchCraftStone"

    def add_resources(self):
        return None

    def add_barriers(self):
        for i in range(50):
            for j in range(10):
                if i == 0 or i == 49 or j == 0 or j == 9:
                    self.Map[i][j] = "9999"

    def add_units(self, class_first, class_second):
        for i in range(20):
            unit_level = randint(1, 7)
            first = 0
            second = 0
            while self.Map[first][second] is not None:
                first = randint(1, 49)
                second = randint(1, 9)
            if unit_level == 1:
                self.Map[first][second] = class_first.first_creature.name
            elif unit_level == 2:
                self.Map[first][second] = class_first.second_creature.name
            elif unit_level == 3:
                self.Map[first][second] = class_first.third_creature.name
            elif unit_level == 4:
                self.Map[first][second] = class_first.fourth_creature.name
            elif unit_level == 5:
                self.Map[first][second] = class_first.fifth_creature.name
            elif unit_level == 7:
                self.Map[first][second] = class_first.sixth_creature.name
