from Units.unit import Unit


class SecondNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Blood Maiden",  # name
                         4,  # attack
                         2,  # protection
                         5,  # min_damage
                         7,  # max_damage
                         16,  # health
                         14,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         125,  # cost
                         50,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)


class SecondUpgraded(Unit):
    def __init__(self):
        super().__init__("Blood Fury",  # name
                         5,  # attack
                         3,  # protection
                         5,  # min_damage
                         7,  # max_damage
                         16,  # health
                         16,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         175,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
