from Units.unit import Unit


class ThirdNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Minotaur",  # name
                         5,  # attack
                         2,  # protection
                         4,  # min_damage
                         7,  # max_damage
                         31,  # health
                         8,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         140,  # cost
                         60,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class ThirdUpgraded(Unit):
    def __init__(self):
        super().__init__("Minotaur Guard",  # name
                         5,  # attack
                         2,  # protection
                         4,  # min_damage
                         7,  # max_damage
                         35,  # health
                         8,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         200,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
