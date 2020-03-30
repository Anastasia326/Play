from Units.unit import Unit


class SixthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Cavalier",  # name
                         23,  # attack
                         21,  # protection
                         20,  # min_damage
                         30,  # max_damage
                         90,  # health
                         11,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         1300,  # cost
                         400,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class SixthUpgraded(Unit):
    def __init__(self):
        super().__init__("Paladin",  # name
                         24,  # attack
                         24,  # protection
                         20,  # min_damage
                         30,  # max_damage
                         100,  # health
                         12,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         1700,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
