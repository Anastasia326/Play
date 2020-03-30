from Units.unit import Unit


class ThirdNotUpgraded(Unit):
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
