from Units.unit import Unit


class SixthNotUpgraded(Unit):
    """
    Биография:
        Являясь живым олицетворением леса, Treants покинули девственные леса по
        призыву наиболее могущественных Druids. Говорят, что когда первые Elves
        осмелились проникнуть в самое сердце девственного первородного леса,
        они нашли там Treants, которые ждали их и были готовы были поклясться
        в своей вечной лояльности. Не дайте себя обмануть их неуклюжей
        походкой - их прочные тела не так-то просто ранить, а любое вражеское
        существо, которые будет им противостоять, будет тут же опутано лианами,
        корнями и ветвями.
    """
    def __init__(self):
        super().__init__("Treant",  # name
                         19,  # attack
                         27,  # protection
                         7,  # min_damage
                         17,  # max_damage
                         175,  # health
                         7,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         1100,  # cost
                         300,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class SixthUpgraded(Unit):
    """
    Биография:
        Сам лес поднялся, чтобы помочь Elves в войне. Медленные, но необычайно
        сильные Ancient Treants связывают своих врагов лианами, корнями и
        ветвями, а также у них есть умение закопать свои корни глубже, что
        усложняет возможность их победить.
    """
    def __init__(self):
        super().__init__("Ancient Treant",  # name
                         19,  # attack
                         29,  # protection
                         10,  # min_damage
                         20,  # max_damage
                         181,  # health
                         7,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         1400,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
