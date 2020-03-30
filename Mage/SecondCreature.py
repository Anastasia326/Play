from Units.unit import Unit


class SecondNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Stone Gargoyle",  # name
                         3,  # attack
                         4,  # protection
                         1,  # min_damage
                         1,  # max_damage
                         15,  # health
                         9,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         40,  # cost
                         30,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)


class SecondUpgraded(Unit):
    def __init__(self):
        super().__init__("Obsidian Gargoyle",  # name
                         3,  # attack
                         5,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         20,  # health
                         10,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         70,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
