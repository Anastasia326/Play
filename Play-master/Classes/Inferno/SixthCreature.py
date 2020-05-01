from Units.unit import Unit


class SixthNotUpgraded(Unit):
    """
    Биография:
        Могучие Pit Fiends приходят из черных глубин преисподней, чтобы служить
        своим хозяевам. Они одинаково искусны и в ближнем бою и в магических
        атаках.
    """
    def __init__(self):
        super().__init__("Pit Fiend",  # name
                         21,  # attack
                         21,  # protection
                         13,  # min_damage
                         26,  # max_damage
                         110,  # health
                         8,  # initiative
                         4,  # speed
                         None,  # shots
                         10,  # mana
                         1400,  # cost
                         266,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class SixthUpgraded(Unit):
    """
    Биография:
        Эти могучие создания призываются из самых дальних глубин демонического
        королевства. Они одинаково искусны и в ближнем бою и в магических
        атаках. Pit Lords несут Vorpal Sword, его тёмная сила тут же убивает
        любое существо, которое выбрало неудачный момент, чтобы противостоять
        ему.
    """
    def __init__(self):
        super().__init__("Pit Lord",  # name
                         22,  # attack
                         21,  # protection
                         13,  # min_damage
                         31,  # max_damage
                         120,  # health
                         8,  # initiative
                         4,  # speed
                         None,  # shots
                         20,  # mana
                         1666,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
