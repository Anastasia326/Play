from abc import ABC, abstractmethod


class Hero(ABC):
    """
    Инициализация класса героя (руководителя войск)

    Характеристики героя:
        - Изученные заклинания
        - Нападение (увеличивает урон существ)
        - Защита (уменьшает урон, наносимый существам)
        - Боевой дух (шанс на продвижение по шкале инициативы)
        - Удача (шанс нанести увеличенный урон)
        - Колдовство (определяет эффективность заклинания)
        - Знание (влияет на количество маны и скорость ее востановления)
        - Предметы
        - Армия

    Методы:
        - Создание
        - Изучение заклинания
        - Улучшение характеристие
        - Использовать заклинание
        - Показать доступные заклинания
        - Показать Армию
        - Добавить в армию
        - Удалить из армии
        - Атаковать
        - Ждать

    """
    def __init__(self):
        self.spells = {}
        self.attack = 0
        self.protection = 0
        self.morale = 0
        self.luck = 0
        self.witchcraft = 0
        self.knowledge = 0
        self.items = []
        self.army = []
        self.skills = []

    @abstractmethod
    def learn_spell(self, spell):
        pass

    @abstractmethod
    def improve_skill(self, name_of_skill, points):
        pass

    @abstractmethod
    def cast_spell(self, spell):
        pass

    @abstractmethod
    def show_available_spells(self):
        pass

    @abstractmethod
    def show_army(self):
        pass

    @abstractmethod
    def add_to_army(self):
        pass

    @abstractmethod
    def remove_from_army(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def wait(self):
        pass
