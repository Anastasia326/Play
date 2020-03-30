from Units.unit import Unit


class FourthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Vampire",  # name
                         6,  # attack
                         6,  # protection
                         6,  # min_damage
                         8,  # max_damage
                         30,  # health
                         11,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         250,  # cost
                         100,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FourthUpgraded(Unit):
    def __init__(self):
        super().__init__("Vampire Lord",  # name
                         9,  # attack
                         7,  # protection
                         7,  # min_damage
                         11,  # max_damage
                         35,  # health
                         11,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         350,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
