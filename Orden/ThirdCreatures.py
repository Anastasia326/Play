from Units.unit import Unit


class ThirdNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Footman",  # name
                         4,  # attack
                         8,  # protection
                         2,  # min_damage
                         4,  # max_damage
                         16,  # health
                         8,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         85,  # cost
                         45,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class ThirdUpgraded(Unit):
    def __init__(self):
        super().__init__("Squire",  # name
                         5,  # attack
                         9,  # protection
                         2,  # min_damage
                         5,  # max_damage
                         26,  # health
                         8,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         130,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
