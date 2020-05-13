from Units.unit import Unit
from .Hero_resouces import Resources
from ..imports import building_in_city_cost, building_in_city_types, \
    find_class, resources, produce_count


class City:
    def __init__(self, hero_name, resources_: Resources):
        """
        :param hero_name: Имя владельца
        :param resources_: привязываем ресурсы, чтобы можно было отслеживать
        постройки
        в словаре строений хранится уровень текущего строения
        """
        self.belong_to = hero_name
        self.generator = find_class(hero_name)
        self.building = {
            "First Creature": 0,
            "Second Creature": 0,
            "Third Creature": 0,
            "Fourth Creature": 0,
            "Fifth Creature": 0,
            "Sixth Creature": 0,
            "Seventh Creature": 0
        }
        self.adding_creatures = [0 for i in range(7)]
        self.able_resources = resources_

    def upgrade_building(self, building_name: str):
        if building_name in building_in_city_types:
            self.building[building_name] += 1
            self.able_resources.remove_resources(
                building_in_city_cost[
                    building_in_city_types.index(building_name)
                ]
            )

    def buy_units(self, unit: Unit, count: int):
        spend_resource = [unit.cost * count, 0, 0, 0, 0, 0]
        if hasattr(unit, "special_resource"):
            spend_resource[resources.index(unit.special_resource)] = count
        self.able_resources.remove_resources(spend_resource)

    def upgrade_units(self, unit: Unit):
        spend_resource = [unit.upgrade_cost * unit.count, 0, 0, 0, 0, 0]
        if hasattr(unit, "special_resource"):
            spend_resource[resources.index(unit.special_resource)] = unit.count
        self.able_resources.remove_resources(spend_resource)

    def next_week(self):
        for i in range(len(self.adding_creatures)):
            self.adding_creatures[i] += produce_count[i]
