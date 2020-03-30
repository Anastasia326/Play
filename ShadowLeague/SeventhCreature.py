from Units.unit import Unit


class SeventhNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Shadow Dragon",  # name
                         25,  # attack
                         24,  # protection
                         45,  # min_damage
                         70,  # max_damage
                         200,  # health
                         10,  # initiative
                         9,  # speed
                         None,  # shots
                         None,  # mana
                         3000,  # cost
                         700,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        special resource


class SeventhUpgraded(Unit):
    def __init__(self):
        super().__init__("Black Dragon",  # name
                         30,  # attack
                         30,  # protection
                         45,  # min_damage
                         70,  # max_damage
                         240,  # health
                         10,  # initiative
                         9,  # speed
                         None,  # shots
                         None,  # mana
                         3700,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
