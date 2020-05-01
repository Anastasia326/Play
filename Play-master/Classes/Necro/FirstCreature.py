from Units.unit import Unit


class FirstNotUpgraded(Unit):
    """
    Биография:
        Вооружённые топором и щитом, Skeleton использует свои костяные руки для
        того, чтобы умерщвлять живых. Высокая инициатива позволяет Skeletons
        зачастую атаковать первыми, но их достаточно хрупкие тела не могут
        выдержать серьёзный урон.
    """
    def __init__(self):
        super().__init__("Skeleton",  # name
                         1,  # attack
                         2,  # protection
                         1,  # min_damage
                         1,  # max_damage
                         4,  # health
                         10,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         19,  # cost
                         11,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FirstUpgraded(Unit):
    """
    Биография:
        Вооружённые луком и стрелами, Skeleton Archers атакуют издалека.
        Высокая инициатива позволяет Skeletons зачастую атаковать первыми, но
        их слабый скелет может выдержать лишь маленький урон, перед тем как
        рухнуть.
    """
    def __init__(self):
        super().__init__("Skeleton Archer",  # name
                         1,  # attack
                         2,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         5,  # health
                         10,  # initiative
                         4,  # speed
                         8,  # shots
                         None,  # mana
                         30,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
