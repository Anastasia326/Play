from Units.unit import Unit


class SecondNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Horned Demon",  # name
                         1,  # attack
                         3,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         13,  # health
                         7,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         40,  # cost
                         20,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)


class SecondUpgraded(Unit):
    def __init__(self):
        super().__init__("Horned Overseer",  # name
                         3,  # attack
                         4,  # protection
                         1,  # min_damage
                         4,  # max_damage
                         13,  # health
                         8,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         60,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
