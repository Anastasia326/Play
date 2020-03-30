from Units.unit import Unit


class SecondNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Zombie",  # name
                         1,  # attack
                         2,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         17,  # health
                         6,  # initiative
                         4,  # speed
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
        super().__init__("Plague Zombie",  # name
                         2,  # attack
                         2,  # protection
                         2,  # min_damage
                         3,  # max_damage
                         17,  # health
                         7,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         60,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
