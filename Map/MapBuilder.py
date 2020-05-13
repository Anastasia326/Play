from abc import ABC, abstractmethod

from Battle.army import Army


class MapBuilder(ABC):
    def __init__(self, wight, length, class_first: Army, class_second: Army):
        self.Map = [[]]
        for i in range(length):
            self.Map[0] += ["Road"]
        for j in range(wight - 1):
            self.Map += [self.Map[0][::]]
        self.add_buildings()
        self.add_cities(class_first, class_second)
        self.add_miners()
        self.add_resources()
        self.add_units()
        self.place_heroes(class_first.hero, class_second.hero)
        self.add_barriers()

    @abstractmethod
    def add_cities(self, class_first, class_second):
        pass

    @abstractmethod
    def add_buildings(self):
        pass

    @abstractmethod
    def add_miners(self):
        pass

    @abstractmethod
    def add_units(self):
        pass

    @abstractmethod
    def add_resources(self):
        pass

    @abstractmethod
    def add_barriers(self):
        pass

    @abstractmethod
    def place_heroes(self, first_hero, second_hero):
        pass
