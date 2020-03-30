from Units.unit import Unit


class ThirdNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Ghost",  # name
                         5,  # attack
                         4,  # protection
                         2,  # min_damage
                         4,  # max_damage
                         16,  # health
                         10,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         100,  # cost
                         40,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class ThirdUpgraded(Unit):
    def __init__(self):
        super().__init__("Spectre",  # name
                         5,  # attack
                         4,  # protection
                         4,  # min_damage
                         6,  # max_damage
                         19,  # health
                         10,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         140,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
