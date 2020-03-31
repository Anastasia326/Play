from abc import ABC, abstractmethod


class MapBuilder(ABC):
    def __init__(self, wight, length, class_first, class_second):
        self.Map = [["0"] * wight] * length
        self.add_barriers()
        self.add_buildings()
        self.add_cities(class_first, class_second)
        self.add_miners()
        self.add_resources()
        self.add_units(class_first, class_second)
        self.place_heroes()

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
    def add_units(self, class_first, class_second):
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
