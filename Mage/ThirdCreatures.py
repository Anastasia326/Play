from Units.unit import Unit


class ThirdNotUpgraded(Unit):
    """
    Биография:
        Големы - это древние магические конструкции, которые используются,
        как первичная боевая пехота Серебрянных Городов. Големы вооружены
        двумя длинными зачарованными мечами, а их материал, из которого они
        сделаны, и есть их броня. Железный голем невосприимчивы к замедляющим
        эффектам - они не могут стать ещё более медленным. Они также
        защищены против магии (весь урон от таких атак уменьшается в два раза).
    """
    def __init__(self):
        super().__init__("Iron Golem",  # name
                         5,  # attack
                         5,  # protection
                         3,  # min_damage
                         5,  # max_damage
                         18,  # health
                         7,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         100,  # cost
                         50,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class ThirdUpgraded(Unit):
    """
    Биография:
        Стальные Големы аккуратно опутаны чарами своих создателей. Они почти
        невосприимчивы к магии (весь урон от таких атак уменьшается в четыре
        раза) и намного более смертельны, чем Железные Големы в бою, поскольку
        немедленно отвечают на каждую атаку, направленную против них.
    """
    def __init__(self):
        super().__init__("Steel Golem",  # name
                         6,  # attack
                         6,  # protection
                         5,  # min_damage
                         7,  # max_damage
                         24,  # health
                         7,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         150,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
