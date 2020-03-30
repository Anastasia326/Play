from Units.unit import Unit


class FifthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Djinn",  # name
                         11,  # attack
                         10,  # protection
                         12,  # min_damage
                         14,  # max_damage
                         40,  # health
                         12,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         460,  # cost
                         170,  # upgrade
                         2,  # length
                         2,  # width
                         ,  # spells
                         0)  # count)


class FifthUpgraded(Unit):
    def __init__(self):
        super().__init__("Djinn Sultan",  # name
                         14,  # attack
                         14,  # protection
                         14,  # min_damage
                         19,  # max_damage
                         45,  # health
                         12,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         630,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
