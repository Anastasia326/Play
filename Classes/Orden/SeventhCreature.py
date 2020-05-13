from Units.unit import Unit


class SeventhNotUpgraded(Unit):
    """
    Биография:
        Angels - это живая реинкарнация Elrath в Ashan, и поэтому они являются
        совершенными представителями этой силы. Эти существа Света неистовы в
        битве, а их атаки всегда смертельны. Ангел не может быть убит, если его
        тело было уничтожено, он вернется в форму духа и воссоединится со своим
        хозяином.
    """
    def __init__(self):
        super().__init__("Angel",  # name
                         27,  # attack
                         27,  # protection
                         45,  # min_damage
                         45,  # max_damage
                         180,  # health
                         11,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         2800,  # cost
                         700,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = "Red"


class SeventhUpgraded(Unit):
    """
    Биография:
        Более возвышенней и могущественней Angels только Archangels. Как прямые
        помощники Elrath, они благословлены величайшей силой воскрешать солдат,
        которые пали в битве и дать им ещё шанс послужить своему Knight Lord.
    """
    def __init__(self):
        super().__init__("Archangel",  # name
                         31,  # attack
                         31,  # protection
                         50,  # min_damage
                         50,  # max_damage
                         220,  # health
                         11,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         3500,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = "Red"
