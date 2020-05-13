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
        - Армия

    Методы:
        - Создание
        - Улучшение характеристик
        - Показать доступные заклинания
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
        self.army = [None]*7
        self.movement = 15

    def improve_skill(self, name_of_skill, points) -> str:
        """Улучшение характеристики"""
        if name_of_skill == "morale":
            self.morale += points
        elif name_of_skill == "luck":
            self.luck += points
        elif name_of_skill == "witchcraft":
            self.witchcraft += points
        elif name_of_skill == "attack":
            self.attack += points
        elif name_of_skill == "protection":
            self.protection += points
        elif name_of_skill == "knowledge":
            self.knowledge += points
        return str(self.name) + "nas improved" + str(name_of_skill)  + "by" + str(points) + "points"


    def show_available_spells(self):
        """Я знаю заклинания: """
        return str.spells

    def show_army(self):
        """Армия"""
        for i in range(len(self.army)):
            print(self.army[i])

