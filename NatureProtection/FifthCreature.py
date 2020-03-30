from Units.unit import Unit


class FifthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Unicorn",  # name
                         12,  # attack
                         12,  # protection
                         10,  # min_damage
                         20,  # max_damage
                         57,  # health
                         12,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         630,  # cost
                         270,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class FifthUpgraded(Unit):
    def __init__(self):
        super().__init__("Silver Unicorn",  # name
                         17,  # attack
                         17,  # protection
                         10,  # min_damage
                         20,  # max_damage
                         77,  # health
                         12,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         900,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
