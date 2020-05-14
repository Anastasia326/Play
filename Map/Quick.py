from Battle.army import Army
from Map.MapBuilder import MapBuilder
from .imports import building_array, Buildings_for_class, ways, find_class


class QuickMap(MapBuilder):
    def __init__(self, class_first: Army, class_second: Army):
        self.neutral_first = Buildings_for_class(find_class(
            class_first.hero.name))
        self.neutral_second = Buildings_for_class(find_class(
            class_second.hero.name))
        super().__init__(50, 11, class_first, class_second)


    def add_miners(self):
        return None

    def place_heroes(self, first_hero, second_hero):
        self.Map[5][5] = first_hero.name
        self.Map[44][5] = second_hero.name

    def add_buildings(self):
        for i in range(len(building_array)):
            self.Map[5 - ways[i][0] * 3][5 - ways[i][1] * 3] = \
                building_array[i]
            self.Map[44 - ways[i][0] * 3][5 - ways[i][1] * 3] = \
                building_array[i]

    def add_resources(self):
        return None

    def add_barriers(self):
        for i in range(50):
            for j in range(11):
                if i == 0 or i == 49 or j == 0 or j == 10:
                    self.Map[i][j] = "NoWay"
                elif (i == 4 or i == 6 or i == 43 or i == 45) and j != 5:
                    self.Map[i][j] = "NoWay"
                elif (j == 6 or j == 4) and (i < 5 or i > 44):
                    self.Map[i][j] = "NoWay"

    def add_units(self):
        for i in range(len(building_array) - 1):
            self.Map[44 - ways[i][0] * 2][5 - ways[i][1] * 2] = \
                self.neutral_first.place(i % (len(self.neutral_first.creatures)))
        for i in range(len(building_array)):
            self.Map[5 - ways[i][0] * 2][5 - ways[i][1] * 2] = \
                self.neutral_second.place(i % (len(self.neutral_second.creatures)))
