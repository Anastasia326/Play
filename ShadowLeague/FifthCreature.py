from Units.unit import Unit


class FifthNotUpgraded(Unit):
    """
    Биография:
        Hydras - это ещё одна раса подземных существ, приручённых и покорённых
        Dark Elves. Их происхождение неизвестно, однако судя по всему они имеют
        родственные отношения к Dragons, несмотря на очень ограниченный ум и
        отсутствие магических сил. Однако же, Hydras невероятно сильны, а их
        множественные головы могут одновременно атаковать разных противников.
    """
    def __init__(self):
        super().__init__("Hydra",  # name
                         15,  # attack
                         12,  # protection
                         7,  # min_damage
                         14,  # max_damage
                         80,  # health
                         7,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         550,  # cost
                         250,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class FifthUpgraded(Unit):
    """
    Биография:
         Deep Hydras древнее чем все остальные Hydras и у них шесть голов,
         вместо обычных трёх. Это позволяет им наносить одновременно и больше
         урона и бить больше врагов за одну атаку.
    """
    def __init__(self):
        super().__init__("Deep Hydra",  # name
                         15,  # attack
                         15,  # protection
                         9,  # min_damage
                         14,  # max_damage
                         125,  # health
                         7,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         800,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
