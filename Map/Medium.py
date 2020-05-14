from Battle.army import Army
from Map.MapBuilder import MapBuilder
from .imports import building_array, Buildings_for_class, ways, classes, \
    miner_array, resources, find_class


class MediumMap(MapBuilder):
    def __init__(self, class_first: Army, class_second: Army):
        self.neutral_second = Buildings_for_class(find_class(class_second.hero.name))
        self.neutral_first = Buildings_for_class(find_class(class_first.hero.name))
        super().__init__(100, 20, class_first, class_second)

    def add_miners(self):
        for i in range(len(miner_array)):
            self.Map[20 - ways[i][0] * 4][10 - ways[i][1] * 4] = \
                miner_array[i]
            self.Map[79 - ways[i][0] * 4][10 - ways[i][1] * 4] = \
                miner_array[i]

    def place_heroes(self, first_hero, second_hero):
        self.Map[2][2] = first_hero.name
        self.Map[97][17] = second_hero.name

    def add_buildings(self):
        for i in range(len(building_array)):
            self.Map[5 - ways[i][0] * 4][5 - ways[i][1] * 4] = \
                building_array[i]
            self.Map[93 - ways[i][0] * 4][5 - ways[i][1] * 4] = \
                building_array[i]

    def add_resources(self):
        for i in range(len(resources)):
            obj = resources[i] + "Count" + \
                  ("5" if resources[i] != "Gold" else "1000")
            self.Map[30 - ways[i][0] * 4][5 - ways[i][1] * 4] = obj
            self.Map[67 - ways[i][0] * 4][5 - ways[i][1] * 4] = obj

    def add_barriers(self):
        for i in range(100):
            for j in range(20):
                if i == 0 or i == 99 or j == 0 or j == 19:
                    self.Map[i][j] = "NoWay"
                if self.Map[i][j] in building_array or \
                        self.Map[i][j].split("Count")[0] in resources or \
                        self.Map[i][j] in miner_array:
                    for k in range(8):
                        if self.Map[i + ways[k][0]][j + ways[k][1]] == "Road":
                            self.Map[i + ways[k][0]][j + ways[k][1]] = "NoWay"

    def add_units(self):
        for i in range(len(building_array)):
            self.Map[5 - ways[i][0] * 3][5 - ways[i][1] * 3] = \
                self.neutral_first.place(i % (len(self.neutral_first.creatures)))
        for i in range(len(resources)):
            self.Map[30 - ways[i][0] * 3][5 - ways[i][1] * 3] = \
                self.neutral_first.place(i % (len(self.neutral_first.creatures)))
        for i in range(len(miner_array)):
            self.Map[20 - ways[i][0] * 3][10 - ways[i][1] * 3] = \
                self.neutral_first.place(i % (len(self.neutral_first.creatures)))
        for i in range(len(building_array) - 1):
            self.Map[93 - ways[i][0] * 3][5 - ways[i][1] * 3] = \
                self.neutral_second.place(i %
                                     (len(self.neutral_second.creatures)))
        for i in range(len(resources)):
            self.Map[67 - ways[i][0] * 3][5 - ways[i][1] * 3] = \
                self.neutral_second.place(i %
                                     (len(self.neutral_second.creatures)))
        for i in range(len(miner_array)):
            self.Map[79 - ways[i][0] * 3][10 - ways[i][1] * 3] = \
                self.neutral_second.place(i %
                                     (len(self.neutral_second.creatures)))
