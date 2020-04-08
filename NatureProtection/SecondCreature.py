from Units.unit import Unit


class SecondNotUpgraded(Unit):
    """
    Биография:
        Blade Dancer - это элита среди пехоты лесных солдат. Определённое число
        Elves посвящают свои жизни невероятно сложному боевому искусству,
        известному как Battle Dance. Надеясь больше на уклонение от ударов и
        скорость своих действий, чем на сопротивление и грубую силу, Blade
        Dancers не носят никакой брони, а значит очень уязвимы для атаки врага.
    """
    def __init__(self):
        super().__init__("Blade Dancer",  # name
                         3,  # attack
                         2,  # protection
                         2,  # min_damage
                         5,  # max_damage
                         12,  # health
                         11,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         70,  # cost
                         50,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)


class SecondUpgraded(Unit):
    """
    Биография:
        Прошедшие жёсткую тренировку Battle Dance, лучшие Elven войны, улучшают
        свой боевой стиль настолько, что могут распространять свой удар на всех
        ближайших врагов одновременно.
    """
    def __init__(self):
        super().__init__("War Dancer",  # name
                         5,  # attack
                         3,  # protection
                         3,  # min_damage
                         5,  # max_damage
                         12,  # health
                         15,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         120,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
