from Units.unit import Unit


class FourthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Dark Rider",  # name
                         9,  # attack
                         7,  # protection
                         7,  # min_damage
                         12,  # max_damage
                         40,  # health
                         11,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         300,  # cost
                         150,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count


class FourthUpgraded(Unit):
    def __init__(self):
        super().__init__("Grim Rider",  # name
                         10,  # attack
                         9,  # protection
                         7,  # min_damage
                         14,  # max_damage
                         60,  # health
                         11,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         450,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
