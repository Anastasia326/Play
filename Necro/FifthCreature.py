from Units.unit import Unit


class FifthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Lich",  # name
                         15,  # attack
                         15,  # protection
                         12,  # min_damage
                         17,  # max_damage
                         50,  # health
                         10,  # initiative
                         3,  # speed
                         5,  # shots
                         None,  # mana
                         620,  # cost
                         230,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class FifthUpgraded(Unit):
    def __init__(self):
        super().__init__("Archlich",  # name
                         19,  # attack
                         19,  # protection
                         17,  # min_damage
                         20,  # max_damage
                         55,  # health
                         10,  # initiative
                         3,  # speed
                         6,  # shots
                         16,  # mana
                         850,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
