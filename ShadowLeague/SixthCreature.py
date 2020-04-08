from Units.unit import Unit


class SixthNotUpgraded(Unit):
    """
    Биография:
         Shadow Witches - это жрицы Malassa. Они используют свои плети в
         ближнем бою, но они намного более смертельны, если используют свои
         магические заклинания.
    """
    def __init__(self):
        super().__init__("Shadow Witch",  # name
                         18,  # attack
                         18,  # protection
                         17,  # min_damage
                         24,  # max_damage
                         80,  # health
                         10,  # initiative
                         4,  # speed
                         4,  # shots
                         11,  # mana
                         1400,  # cost
                         300,  # upgrade
                         1,  # length
                         1,  # width
                         {},  # spells
                         0)  # count)


class SixthUpgraded(Unit):
    """
    Биография:
         Shadow Matriarchs - это правящая элита армий Dark Elves. Если их
         вынуждают к ближнему бою, они будут использовать плети, как оружие, но
          предпочитают полагаться на свои более могущественные магические
          способности. Matriarchs применяют больше заклинания, чем Witches.
    """
    def __init__(self):
        super().__init__("Shadow Matriarch",  # name
                         20,  # attack
                         20,  # protection
                         17,  # min_damage
                         27,  # max_damage
                         90,  # health
                         10,  # initiative
                         4,  # speed
                         4,  # shots
                         14,  # mana
                         1700,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         {},  # spells
                         0)  # count)
