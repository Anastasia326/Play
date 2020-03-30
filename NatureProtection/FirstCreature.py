from Units.unit import Unit


class FirstNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Pixie",  # name
                         1,  # attack
                         1,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         5,  # health
                         12,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         35,  # cost
                         20,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FirstUpgraded(Unit):
    def __init__(self):
        super().__init__("Sprite",  # name
                         2,  # attack
                         2,  # protection
                         2,  # min_damage
                         2,  # max_damage
                         6,  # health
                         15,  # initiative
                         7,  # speed
                         None,  # shots
                         10,  # mana
                         55,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
