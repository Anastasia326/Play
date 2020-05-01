from Units.unit import Unit


class FirstNotUpgraded(Unit):
    """
    Биография:
        Peasants - базовая пехота Holy Griffin Empire. Хотя они слабы и очень
        плохо обучены, они выигрывают числом. К тому же, Peasants - это важный
        источник дохода для своих хозяев.
    """
    def __init__(self):
        super().__init__("Villager",  # name
                         1,  # attack
                         1,  # protection
                         1,  # min_damage
                         1,  # max_damage
                         3,  # health
                         8,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         15,  # cost
                         10,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FirstUpgraded(Unit):
    """
    Биография:
        Conscripts - базовая пехота Holy Griffin Empire. Они относительно слабы
        и частично обучены, но они очень многочисленны. Conscripts - эксперты в
        искусстве оглушения своих врагов во время рукопашной атаки.
    """
    def __init__(self):
        super().__init__("Conscript",  # name
                         1,  # attack
                         2,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         6,  # health
                         8,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         25,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)

