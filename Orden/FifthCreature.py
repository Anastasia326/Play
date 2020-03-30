from Units.unit import Unit


class FifthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Priest",  # name
                         12,  # attack
                         12,  # protection
                         9,  # min_damage
                         12,  # max_damage
                         54,  # health
                         10,  # initiative
                         5,  # speed
                         7,  # shots
                         None,  # mana
                         600,  # cost
                         250,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)


class FifthUpgraded(Unit):
    def __init__(self):
        super().__init__("Inquisitor",  # name
                         16,  # attack
                         16,  # protection
                         9,  # min_damage
                         12,  # max_damage
                         80,  # health
                         10,  # initiative
                         5,  # speed
                         7,  # shots
                         12,  # mana
                         850,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
