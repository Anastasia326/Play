from Units.unit import Unit


class FirstNotUpgraded(Unit):
    """
    Биография:
        Imps - маленькие проворные существа, которые достаточно слабы в ближнем
        бою - их сила в их численности. У Imps есть умение Mana Destroyer,
        который позволяет им уничтожать магическую энергию вражеских героев.
    """
    def __init__(self):
        super().__init__("Imp",  # name
                         2,  # attack
                         1,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         4,  # health
                         13,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         25,  # cost
                         20,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FirstUpgraded(Unit):
    """
    Биография:
        Familiars - маленькие проворные существа, которые достаточно слабы в
        ближнем бою - их сила в их численности. Familiars обладают умением Mana
        Stealer, который позволяет им красть магическую энергию у врагов и
        передавать её своему герою.
    """
    def __init__(self):
        super().__init__("Familiar",  # name
                         3,  # attack
                         2,  # protection
                         2,  # min_damage
                         3,  # max_damage
                         6,  # health
                         13,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         45,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
