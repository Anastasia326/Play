from Units.unit import Unit


class FourthNotUpgraded(Unit):
    """
    Биография:
        Некоторые Маги из Серебрянных городов служат в армии героев. Они
        слабы в ближнем бою, будучи вооружены лишь кинжалом, а также абсолютно
        необучены рукопашному бою. Эта их слабость компенсируется, однако,
        силой их заклинаний. Они могут стрелять зарядом чистой магической
        энергии, которая наносит урон любому существу у себя на пути, включая
        дружественных существ. Они также переносят свитки с дополнительными
        заклинаниями на них.
    """
    def __init__(self):
        super().__init__("Mage",  # name
                         10,  # attack
                         10,  # protection
                         7,  # min_damage
                         7,  # max_damage
                         18,  # health
                         10,  # initiative
                         4,  # speed
                         3,  # shots
                         10,  # mana
                         250,  # cost
                         90,  # upgrade
                         1,  # length
                         1,  # width
                         {},  # spells
                         0)  # count


class FourthUpgraded(Unit):
    """
    Биография:
        Наиболее могущественные боевые Маги могут стать Архимагами, что даёт им
        доступ ко многим заклинаниям. Герой, в армии которого присутствуют
        архимаги, тратит меньше маны при применении магических заклинаний.
    """
    def __init__(self):
        super().__init__("Archmage",  # name
                         10,  # attack
                         10,  # protection
                         7,  # min_damage
                         7,  # max_damage
                         30,  # health
                         10,  # initiative
                         4,  # speed
                         4,  # shots
                         25,  # mana
                         340,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         {},  # spells
                         0)  # count)
