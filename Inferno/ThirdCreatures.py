from Units.unit import Unit


class ThirdNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Hell hound",  # name
                         4,  # attack
                         3,  # protection
                         3,  # min_damage
                         5,  # max_damage
                         15,  # health
                         13,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         110,  # cost
                         50,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class ThirdUpgraded(Unit):
    def __init__(self):
        super().__init__("Cerberus",  # name
                         4,  # attack
                         2,  # protection
                         4,  # min_damage
                         6,  # max_damage
                         15,  # health
                         13,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         160,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
