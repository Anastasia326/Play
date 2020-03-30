from Units.unit import Unit


class SixthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Rakshasa Rani",  # name
                         25,  # attack
                         20,  # protection
                         15,  # min_damage
                         23,  # max_damage
                         120,  # health
                         9,  # initiative
                         5,  # speed
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
        super().__init__("Rakshasa Raja",  # name
                         25,  # attack
                         20,  # protection
                         23,  # min_damage
                         30,  # max_damage
                         140,  # health
                         8,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         1700,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
