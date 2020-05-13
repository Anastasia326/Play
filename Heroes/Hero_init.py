from abc import ABC, abstractmethod

from Map.imports import hero_characteristics


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
        - Армия

    Методы:
        - Создание
        - Улучшение характеристик
        - Показать Армию
        - Добавить в армию
        - Удалить из армии
        - Атаковать

    """

    def __init__(self, name, spells, attack, protection, morale, luck,
                 witchcraft, knowledge):
        self.name = name
        self.spells = spells
        self.attack = attack
        self.protection = protection
        self.morale = morale
        self.luck = luck
        self.witchcraft = witchcraft
        self.knowledge = knowledge
        self.movement = 15

    def improve_skill(self, name_of_skill, points) -> str:
        """Улучшение характеристики"""
        if name_of_skill in hero_characteristics:
            self.__setattr__(
                name_of_skill,
                self.__getattribute__(name_of_skill) + int(points)
            )
            return str(self.name) + "nas improved" + str(
                name_of_skill) + "by" + str(points) + "points"

    def show_army(self):
        """Армия"""
        for i in range(len(self.army)):
            print(self.army[i])
