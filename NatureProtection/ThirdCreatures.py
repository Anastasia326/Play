from Units.unit import Unit


class ThirdNotUpgraded(Unit):
    """
    Биография:
        В мирное время, Hunters обеспечивают общество Sylvan едой, и они весьма
        уважаемы за их способности и отвагу. Странствуя по Irollan, они живут в
        гармонии с Природой и её неписанными законами. Они никогда не убьют
        живое существо просто так. Однако, в военное же время, они без
        сожаления используют свои таланты для уничтожения врагов издалека. Их
        необъяснимое сращивание в единое целое с их зачарованными Elf Bows
        позволяет им стрелять дважды, ещё до того, как соперник успеет моргнуть
    """
    def __init__(self):
        super().__init__("Hunter",  # name
                         4,  # attack
                         1,  # protection
                         5,  # min_damage
                         7,  # max_damage
                         10,  # health
                         10,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         120,  # cost
                         70,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class ThirdUpgraded(Unit):
    """
    Биография:
        Master Hunters посвящают свою жизнь обороне лесных царств и поднимаются
        как один, чтобы защитить его от посягательств любых чужаков.
        Специальное колдовство, наложенное на их стрелы и луки позволяет им
        выстрелить дважды ещё даже до того, как враг поймёт, что они здесь, а
        также гарантирует, что цель будет выздоравливать очень медленно после
        их атаки.
    """
    def __init__(self):
        super().__init__("Master Hunter",  # name
                         5,  # attack
                         4,  # protection
                         5,  # min_damage
                         9,  # max_damage
                         14,  # health
                         10,  # initiative
                         5,  # speed
                         16,  # shots
                         None,  # mana
                         190,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
