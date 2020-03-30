from Units.unit import Unit


class FifthNotUpgraded(Unit):
    def __init__(self):
        super().__init__("Hell Charger",  # name
                         13,  # attack
                         13,  # protection
                         8,  # min_damage
                         16,  # max_damage
                         50,  # health
                         16,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         550,  # cost
                         230,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class FifthUpgraded(Unit):
    def __init__(self):
        super().__init__("Nightmare",  # name
                         18,  # attack
                         18,  # protection
                         8,  # min_damage
                         16,  # max_damage
                         66,  # health
                         16,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         780,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
