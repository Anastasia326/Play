from Units.unit import Unit


class SeventhNotUpgraded(Unit):
    """
    Биография:
          Выкраденные из своих гробниц и вынужденные служить Necromancers,
          Bone Dragons создают из скелетов мертвых драконов других пород.
          В землях Necromancer нет природных драконов, поэтому им приходиться
          выкрадывать их в других областях и делать их самостоятельно.
    """
    def __init__(self):
        super().__init__("Bone Dragon",  # name
                         27,  # attack
                         28,  # protection
                         15,  # min_damage
                         30,  # max_damage
                         150,  # health
                         11,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         1600,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = 1


class SeventhUpgraded(Unit):
    """
    Биография:
        На тело призрачного дракона пошли кости не одного вида драконов. Чтобы
        создать такую жуткую тварь, пришлось взять кости всех видов обычных
        драконов, соединить между собой особым образом в единый скелет и затем
        в получившееся вдохнуть нежизнь, пожертвовав душу высокопоставленного
        некроманта.
    """
    def __init__(self):
        super().__init__("Spectral Dragon",  # name
                         30,  # attack
                         28,  # protection
                         25,  # min_damage
                         35,  # max_damage
                         160,  # health
                         11,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         1900,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = 1
