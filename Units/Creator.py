from abc import ABC, abstractmethod


class Creator(ABC):
    """
    Наша абстрактная фабрика, которая рождена, дабы создавать фракции
    Соответсвующее создание юнитов и героев реализовано в фабриках
    Предоставляет интерфейс
    """
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
    def create_hero(self):
        pass

    '''
    Остановись и подумай о создании города и соответствующих зданий
    '''
