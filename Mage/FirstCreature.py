from Units.unit import Unit


class FirstNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Gremlin",  # name
                         2,  # attack
                         2,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         5,  # health
                         7,  # initiative
                         3,  # speed
                         5,  # shots
                         None,  # mana
                         22,  # cost
                         13,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FirstUpgraded(Unit):
    def __init__(self):
        super().__init__("Master Gremlin",  # name
                         2,  # attack
                         2,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         6,  # health
                         11,  # initiative
                         5,  # speed
                         7,  # shots
                         None,  # mana
                         35,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
