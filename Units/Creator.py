from abc import ABC, abstractmethod


class Creator(ABC):
    """
    Наша абстрактная фабрика, которая рождена, дабы создавать фракции
    Соответсвующее создание юнитов и героев реализовано в фабриках
    Предоставляет интерфейс
    """
    def __init__(self):
        self.first_creature = None
        self.second_creature = None
        self.third_creature = None
        self.fourth_creature = None
        self.fifth_creature = None
        self.sixth_creature = None
        self.seventh_creature = None
        self.first_creature_upgraded = None
        self.second_creature_upgraded = None
        self.third_creature_upgraded = None
        self.fourth_creature_upgraded = None
        self.fifth_creature_upgraded = None
        self.sixth_creature_upgraded = None
        self.seventh_creature_upgraded = None
        self.create_first_type_creatures()
        self.create_second_type_creatures()
        self.create_third_type_creatures()
        self.create_fourth_type_creatures()
        self.create_fifth_type_creatures()
        self.create_sixth_type_creatures()
        self.create_seventh_type_creatures()
        self.create_hero_First()
        self.reate_hero_Second()

    @abstractmethod
    def create_first_type_creatures(self):
        pass

    @abstractmethod
    def create_second_type_creatures(self):
        pass

    @abstractmethod
    def create_third_type_creatures(self):
        pass

    @abstractmethod
    def create_fourth_type_creatures(self):
        pass

    @abstractmethod
    def create_fifth_type_creatures(self):
        pass

    @abstractmethod
    def create_sixth_type_creatures(self):
        pass

    @abstractmethod
    def create_seventh_type_creatures(self):
        pass

    @abstractmethod
    def create_hero_First(self):
        pass

    @abstractmethod
    def create_hero_Second(self):
        pass

