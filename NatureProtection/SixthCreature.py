from Units.unit import Unit


class SixthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Treant",  # name
                         19,  # attack
                         27,  # protection
                         7,  # min_damage
                         17,  # max_damage
                         175,  # health
                         7,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         1100,  # cost
                         300,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class SixthUpgraded(Unit):
    def __init__(self):
        super().__init__("Ancient Treant",  # name
                         19,  # attack
                         29,  # protection
                         10,  # min_damage
                         20,  # max_damage
                         181,  # health
                         7,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         1400,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
