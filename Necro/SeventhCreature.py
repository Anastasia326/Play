from Units.unit import Unit


class SeventhNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Bone Dragon",  # name
                         27,  # attack
                         28,  # protection
                         15,  # min_damage
                         30,  # max_damage
                         150,  # health
                         11,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         1600,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = 1


class SeventhUpgraded(Unit):
    def __init__(self):
        super().__init__("Spectral Dragon",  # name
                         30,  # attack
                         28,  # protection
                         25,  # min_damage
                         35,  # max_damage
                         160,  # health
                         11,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         1900,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = 1
