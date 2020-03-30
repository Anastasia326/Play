from Units.unit import Unit


class ThirdNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Iron Golem",  # name
                         5,  # attack
                         5,  # protection
                         3,  # min_damage
                         5,  # max_damage
                         18,  # health
                         7,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         100,  # cost
                         50,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class ThirdUpgraded(Unit):
    def __init__(self):
        super().__init__("Steel Golem",  # name
                         6,  # attack
                         6,  # protection
                         5,  # min_damage
                         7,  # max_damage
                         24,  # health
                         7,  # initiative
                         4,  # speed
                         None,  # shots
                         None,  # mana
                         150,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
