from ArmyGenerator.GenerateInferno import inferno
from ArmyGenerator.GenerateMage import mage
from ArmyGenerator.GenerateNature import Nature
from ArmyGenerator.GenerateNecropolis import necro
from ArmyGenerator.GenerateOrden import orden
from ArmyGenerator.GenerateShadowLeague import Shadow
from Units.Creator import Creator

building_array = [
    "Camp",
    "MagicStone",
    "DefenseBuilding",
    "WitchCraftStone"
]

improving_skills_list = [
    "attack",
    "knowledge",
    "protection",
    "witchcraft"
]

miner_array = ["Gold_Miner",
               "Red_Miner",
               "Yellow_Miner",
               "Blue_Miner",
               "Wood_Miner",
               "Stone_Miner"
               ]

resources = ["Gold",
             "Red",
             "Yellow",
             "Blue",
             "Wood",
             "Stone"
             ]


class Buildings_for_class:
    def __init__(self, army: Creator):
        self.creatures = []
        army.first_creature.count = 40
        self.creatures += [army.first_creature]
        army.second_creature.count = 20
        self.creatures += [army.second_creature]
        army.third_creature.count = 10
        self.creatures += [army.third_creature]

    def place(self, index):
        if index < 3:
            return self.creatures[index].name
        else:
            return "Wrong"


ways = [[0, 1],
        [-1, 0],
        [0, -1],
        [1, 0],
        [1, 1],
        [-1, -1],
        [1, -1],
        [-1, 1]]

orden_ = orden()
mage_ = mage()
shadow_ = Shadow()
inferno_ = inferno()
nature_ = Nature()
necro_ = necro()

classes = [
    orden_,
    mage_,
    shadow_,
    inferno_,
    nature_,
    necro_
]


def find_class(hero_name):
    for class_ in classes:
        if hero_name == class_.first_hero.name or hero_name == \
                class_.second_hero.name:
            return class_


building_in_city_types = [
    "First Creature",
    "Second Creature",
    "Third Creature",
    "Fourth Creature",
    "Fifth Creature",
    "Sixth Creature",
    "Seventh Creature"
]

produce_count = [22, 16, 12, 8, 6, 4, 2]

building_in_city_cost = [
    [1000, 2, 2, 0, 0, 0],
    [2000, 4, 4, 2, 0, 0],
    [2500, 3, 2, 0, 2, 0],
    [1000, 2, 5, 2, 0, 2],
    [4000, 1, 1, 1, 1, 1],
    [5000, 2, 2, 2, 2, 2]
]

hero_characteristics = [
    "morale",
    "luck",
    "witchcraft",
    "attack",
    "protection",
    "knowledge"
]
