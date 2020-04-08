from Units.unit import Unit


class FifthNotUpgraded(Unit):
    """
    Биография:
        Priests - это хранители религиозной веры в Griffin Empire. Они свирепо
        воюют с теми, кто не разделяет их веру и с любым, кто угрожает
        Church of Elrath. Priests не очень сильны в рукопашной схватке на поле
        боя, но вместо этого они могут призвать с небес гнев богов на головы
        солдат врагов.
    """
    def __init__(self):
        super().__init__("Priest",  # name
                         12,  # attack
                         12,  # protection
                         9,  # min_damage
                         12,  # max_damage
                         54,  # health
                         10,  # initiative
                         5,  # speed
                         7,  # shots
                         None,  # mana
                         600,  # cost
                         250,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)


class FifthUpgraded(Unit):
    """
    Биография:
        Инквизиторы - это хранители истинной веры в Эрлата - в Священного
        Дракона Света. Они свирепо воюют с теми, кто не разделяет их веру и с
        любым, кто угрожает Церкви Эрлата. На поле боя инквизиторы не вступают
        в рукопашный бой, но способны призывать гнев Эрлата на головы врагов, и
        в то же время защищают себя с помощью заклинаний.
    """
    def __init__(self):
        super().__init__("Inquisitor",  # name
                         16,  # attack
                         16,  # protection
                         9,  # min_damage
                         12,  # max_damage
                         80,  # health
                         10,  # initiative
                         5,  # speed
                         7,  # shots
                         12,  # mana
                         850,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
