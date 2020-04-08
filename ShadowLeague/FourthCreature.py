from Units.unit import Unit


class FourthNotUpgraded(Unit):
    """
    Биография:
         Наездники на ящерах — это спинной хребет армий Игг-Шайла. Это хорошо
         обученные верховые воины, которых носят могучие ящеры. Их основным
         оружием является копье и щит. Скорость — главное оружие наездников,
         ибо урон, наносимый противнику копьем, зависит от расстояния,
         пройденного ими во время разбега.
    """
    def __init__(self):
        super().__init__("Dark Rider",  # name
                         9,  # attack
                         7,  # protection
                         7,  # min_damage
                         12,  # max_damage
                         40,  # health
                         11,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         300,  # cost
                         150,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count


class FourthUpgraded(Unit):
    """
    Биография:
         Темные всадники схожи со своими менее сильными братьями. Однако они
         гораздо более умелые, а их ящеры обучены кусать противника.
    """
    def __init__(self):
        super().__init__("Grim Rider",  # name
                         10,  # attack
                         9,  # protection
                         7,  # min_damage
                         14,  # max_damage
                         60,  # health
                         11,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         450,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
