from Units.unit import Unit


class ThirdNotUpgraded(Unit):
    """
    Биография:
        Ярость заставляет Hell Hound передвигаться по полю боя быстрее, атакуя
        с силой и злобой. Однако, их ярость на поле боя, также и их слабость.
        Hell Hounds мало заботятся о собственной безопасности, что делает их
        уязвимыми, поскольку они фокусируют всю свою энергию на атаке.
    """
    def __init__(self):
        super().__init__("Hell hound",  # name
                         4,  # attack
                         3,  # protection
                         3,  # min_damage
                         5,  # max_damage
                         15,  # health
                         13,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         110,  # cost
                         50,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class ThirdUpgraded(Unit):
    """
    Биография:
        Ярость заставляет Cerberus передвигаться по полю боя быстрее, атакуя с
        силой и злобой, но за ярость они платят осторожностью и своей защитой.
        От атаки Cerberus невозможно защититься, а их трехголовый мульти-удар
        не позволяет соперникам отвечать.
    """
    def __init__(self):
        super().__init__("Cerberus",  # name
                         4,  # attack
                         2,  # protection
                         4,  # min_damage
                         6,  # max_damage
                         15,  # health
                         13,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         160,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
