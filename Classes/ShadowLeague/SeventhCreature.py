from Units.unit import Unit


class SeventhNotUpgraded(Unit):
    """
    Биография:
        Shadow Dragons живут в глубинах массивных пещер в далёких подземельях.
        Будучи объектом поклонения общества Dark Elves, как воплощение их Great
        Mother, они допускают к себе свои почитателей и иногда выступают в
        союзе с ними. Даже один Shadow Dragon - ужасный противник,
        его дыхание - волна негативной энергии, которая может истощить силы,
        даже наиболее стойких врагов.
    """
    def __init__(self):
        super().__init__("Shadow Dragon",  # name
                         25,  # attack
                         24,  # protection
                         45,  # min_damage
                         70,  # max_damage
                         200,  # health
                         10,  # initiative
                         9,  # speed
                         None,  # shots
                         None,  # mana
                         3000,  # cost
                         700,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = "Red"


class SeventhUpgraded(Unit):
    """
    Биография:
        Black Dragons наиболее древние и самые могущественные из всех братьев
        и сестёр Shadow Dragons. В дополнение к тем умениям, которыми обладают
        их более слабые братья, Black Dragons сильнее и имеют абсолютный
        иммунитет к магии.
    """
    def __init__(self):
        super().__init__("Black Dragon",  # name
                         30,  # attack
                         30,  # protection
                         45,  # min_damage
                         70,  # max_damage
                         240,  # health
                         10,  # initiative
                         9,  # speed
                         None,  # shots
                         None,  # mana
                         3700,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = "Red"
