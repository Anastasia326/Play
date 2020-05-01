from Units.unit import Unit


class SecondNotUpgraded(Unit):
    """
    Биография:
        Zombies - это гнилые тела, поднятые Necromancers для того, чтобы
        принести смерть и разрушения врагам. Хотя они очень медленные и
        неуклюжие, Zombies не чувствуют боли и страха. Это позволяет им
        запугивать врагов. По сути, это идеальное пушечное мясо.
    """
    def __init__(self):
        super().__init__("Zombie",  # name
                         1,  # attack
                         2,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         17,  # health
                         6,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         40,  # cost
                         20,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)


class SecondUpgraded(Unit):
    """
    Биография:
        Plague Zombies - это гнилые тела поднятые Necromancers для того, чтобы
        сеять смерть среди врагов. Plague Zombies не чувствуют боли и могут
        выдержать огромное количество ударов. В дополнение ко всему, их гнилое
        оружие может заразить любое живое существо изнуряющей болезнью.
    """
    def __init__(self):
        super().__init__("Plague Zombie",  # name
                         2,  # attack
                         2,  # protection
                         2,  # min_damage
                         3,  # max_damage
                         17,  # health
                         7,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         60,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
