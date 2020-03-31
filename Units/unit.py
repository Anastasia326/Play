from abc import ABC
from _collections import OrderedDict


class Unit(ABC):
    """
    Юнит хранит информацию о юнитах(войсках)

    Характеристики существ:
        - Атака существа
        - Защита существа
        - минимальный наносимый урон
        - максимальный наносимый урон
        - жизни одного существа
        - Инициатива существа (влияет на скорость повторного хода существа)
        - Скорость существа (определяет дальность его перемещения)
        - Количество досутпных выстрелов (Сколько стрел в колчане)
        - Запас маны (у существ, имеющих заклинания)
        - было ли улучшено существо
        - стоимость 1 экземпляра юнита
        - стоимость улучшения одного экземпляра юнита
        - ширина юнита(занимаемое место)
        - длина
        - заклинания(если есть)
        - Расположение на боевой площадке
        - Полученные улучшения и их длительность
        - Какие параметры были улушены, насколько, в каком порядке

    Методы:
        - Инициализация (установление изначальных параметров существа)
        - Получение урона
        - Передвижение
        - Ждать
        - Обороняться
    """

    def __init__(self, name, attack, protection, min_damage, max_damage,
                 health, initiative, speed, shots, mana, cost, upgrade,
                 length, width, spells, count):
        self.name = name
        self.attack = attack
        self.protection = protection
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.health_points = health
        self.initiative = initiative
        self.speed = speed
        self.shots = shots
        self.mana = mana
        self.cost = cost
        self.upgrade_cost = upgrade
        self.length = length
        self.width = width
        self.spells = spells
        self.position_on_battle_ground = [0, 0]
        self.improvement_duration = OrderedDict
        self.improvement_characteristics = OrderedDict
        self.count = count
        self.last_creature_hp = health

    @staticmethod
    def add_count(self, count) -> str:
        """Добавление существ"""
        self.count += count
        return str(count) + " " + str(self.name) + " was added"

    def get_damaged(self, damage) -> str:
        """Получение урона существом"""
        if (self.count - 1) * self.health_points + self.last_creature_hp <= \
                damage:
            self.count = 0
            self.last_creature_hp = 0
            return str(self.name) + " is dead"
        else:
            tmp = (self.count - 1) * self.health_points + \
                  self.last_creature_hp - damage
            log = self.count
            self.count = tmp // self.health_points + (tmp %
                                                      self.health_points > 0)
            log -= self.count
            if tmp % self.health_points == 0:
                self.last_creature_hp = self.health_points
            else:
                self.last_creature_hp = tmp % self.health_points
            return str(log) + " " + str(self.name) + " died. " + str(
                damage) + " was taken"

    def move(self, to) -> str:
        """Передвижение существа"""
        self.position_on_battle_ground = to
        return str(self.name) + " moved to" + str(
            self.position_on_battle_ground[0]) + " " + str(
            self.position_on_battle_ground[1])

    def wait(self) -> str:
        """Юнит ожидает"""
        self.improvement_characteristics += {"Wait", 3}
        self.initiative += 3
        self.improvement_duration += {"Wait", 1}
        return str(self.name) + " is waiting"

    def defend(self) -> str:
        """Оборона"""
        self.protection = int(self.protection * 1.3) + \
                          (self.protection * 1.3 - int(
                              self.protection * 1.3) >= 0.5)
        self.improvement_characteristics += {"Defend", 3}
        self.improvement_duration += {"Defend", 1}
        return str(self.name) + " is defending"
