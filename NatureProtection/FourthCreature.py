from Units.unit import Unit


class FourthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Druid",  # name
                         7,  # attack
                         7,  # protection
                         7,  # min_damage
                         9,  # max_damage
                         34,  # health
                         10,  # initiative
                         5,  # speed
                         5,  # shots
                         12,  # mana
                         320,  # cost
                         120,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FourthUpgraded(Unit):
    def __init__(self):
        super().__init__("Druid Elder",  # name
                         12,  # attack
                         9,  # protection
                         9,  # min_damage
                         14,  # max_damage
                         33,  # health
                         10,  # initiative
                         4,  # speed
                         7,  # shots
                         15,  # mana
                         440,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
