from Units.unit import Unit


class SeventhNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Angel",  # name
                         27,  # attack
                         27,  # protection
                         45,  # min_damage
                         45,  # max_damage
                         180,  # health
                         11,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         2800,  # cost
                         700,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        special resource


class SeventhUpgraded(Unit):
    def __init__(self):
        super().__init__("Archangel",  # name
                         31,  # attack
                         31,  # protection
                         50,  # min_damage
                         50,  # max_damage
                         220,  # health
                         11,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         3500,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
