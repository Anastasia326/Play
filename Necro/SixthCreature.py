from Units.unit import Unit


class SixthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Wight",  # name
                         24,  # attack
                         22,  # protection
                         21,  # min_damage
                         25,  # max_damage
                         95,  # health
                         11,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         1400,  # cost
                         300,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class SixthUpgraded(Unit):
    def __init__(self):
        super().__init__("Wraith",  # name
                         26,  # attack
                         24,  # protection
                         25,  # min_damage
                         30,  # max_damage
                         100,  # health
                         11,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         1700,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
