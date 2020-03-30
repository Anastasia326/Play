from Units.unit import Unit


class FourthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Mage",  # name
                         10,  # attack
                         10,  # protection
                         7,  # min_damage
                         7,  # max_damage
                         18,  # health
                         10,  # initiative
                         4,  # speed
                         3,  # shots
                         10,  # mana
                         250,  # cost
                         90,  # upgrade
                         1,  # length
                         1,  # width
                         ,  # spells
                         0)  # count


class FourthUpgraded(Unit):
    def __init__(self):
        super().__init__("Archmage",  # name
                         10,  # attack
                         10,  # protection
                         7,  # min_damage
                         7,  # max_damage
                         30,  # health
                         10,  # initiative
                         4,  # speed
                         4,  # shots
                         25,  # mana
                         340,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         ,  # spells
                         0)  # count)
