from Units.unit import Unit


class SeventhNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Green Dragon",  # name
                         27,  # attack
                         25,  # protection
                         30,  # min_damage
                         50,  # max_damage
                         200,  # health
                         12,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         2500,  # cost
                         900,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = 1


class SeventhUpgraded(Unit):
    def __init__(self):
        super().__init__("Emerald Dragon",  # name
                         31,  # attack
                         27,  # protection
                         33,  # min_damage
                         57,  # max_damage
                         200,  # health
                         14,  # initiative
                         9,  # speed
                         None,  # shots
                         None,  # mana
                         3400,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = 1
