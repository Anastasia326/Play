from Units.unit import Unit


class FourthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Succubus",  # name
                         6,  # attack
                         6,  # protection
                         6,  # min_damage
                         13,  # max_damage
                         20,  # health
                         10,  # initiative
                         4,  # speed
                         6,  # shots
                         None,  # mana
                         240,  # cost
                         110,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FourthUpgraded(Unit):
    def __init__(self):
        super().__init__("Succubus Mistress",  # name
                         6,  # attack
                         6,  # protection
                         6,  # min_damage
                         13,  # max_damage
                         30,  # health
                         10,  # initiative
                         4,  # speed
                         6,  # shots
                         None,  # mana
                         350,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
