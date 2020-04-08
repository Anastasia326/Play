from Units.unit import Unit


class FourthNotUpgraded(Unit):
    """
    Биография:
        Griffins одни из быстрейших солдат в Griffin Empire, которая носит их
        имя. Они непревзойденные бойцы в быстрых рейдах, врываясь налету в ряды
        противника. Хотя, они довольно слабы, когда вынуждены перейти к
        рукопашной схватке, но они всегда будут защищать себя до последнего
        издыхания.
    """
    def __init__(self):
        super().__init__("Griffin",  # name
                         7,  # attack
                         5,  # protection
                         5,  # min_damage
                         10,  # max_damage
                         30,  # health
                         15,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         260,  # cost
                         110,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count


class FourthUpgraded(Unit):
    """
    Биография:
        Imperial Griffins самые быстрые солдаты Griffin Empire. Они превосходны
        в быстрых рейдах, разрывая налету стройные ряды врагов или бросаясь с
        небес во время битвы.
    """
    def __init__(self):
        super().__init__("Imperial Griffin",  # name
                         9,  # attack
                         8,  # protection
                         5,  # min_damage
                         15,  # max_damage
                         35,  # health
                         15,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         370,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
