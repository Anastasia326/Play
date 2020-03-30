from Units.unit import Unit


class SecondNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Archer",  # name
                         4,  # attack
                         3,  # protection
                         2,  # min_damage
                         4,  # max_damage
                         7,  # health
                         9,  # initiative
                         4,  # speed
                         10,  # shots
                         None,  # mana
                         50,  # cost
                         30,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)


class SecondUpgraded(Unit):
    def __init__(self):
        super().__init__("Marksman",  # name
                         4,  # attack
                         4,  # protection
                         2,  # min_damage
                         8,  # max_damage
                         10,  # health
                         8,  # initiative
                         4,  # speed
                         12,  # shots
                         None,  # mana
                         80,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
