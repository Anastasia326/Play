from Units.unit import Unit


class SeventhNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Colossus",  # name
                         27,  # attack
                         27,  # protection
                         40,  # min_damage
                         70,  # max_damage
                         175,  # health
                         10,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         2700,  # cost
                         600,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        special resource


class SeventhUpgraded(Unit):
    def __init__(self):
        super().__init__("Titan",  # name
                         30,  # attack
                         30,  # protection
                         40,  # min_damage
                         70,  # max_damage
                         190,  # health
                         10,  # initiative
                         6,  # speed
                         5,  # shots
                         None,  # mana
                         3300,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
