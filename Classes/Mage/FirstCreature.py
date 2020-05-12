from Units.unit import Unit


class FirstNotUpgraded(Unit):
    """
    Биография:
        Существа, рождённые в результате магических экспериментов над попавшими
         в плен Гоблинами, Гремлины более сообразительны и покорны, нежели их
        прародители. Гремлин - это наиболее часто встречающееся существо,
        в армии Магов, которое предпочитает сражаться на расстоянии, используя
        примитивные стрелковые приспособления, заряженные взрывающимися
        заклинаниями. Эти неповоротливые ручные мортиры очень прочны, и во
        время рукопашной схватки Гремлины используют их как дубинки.
    """
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
    """
    Биография:
         Гремлины, которые отличились на поле боя могут быть произведены в ранг
         Мастеров Гремлинов. Они обучены чинить разные механизмы (Балисту,
         Големов и т.д.).
    """
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
