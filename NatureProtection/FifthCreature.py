from Units.unit import Unit


class FifthNotUpgraded(Unit):
    """
    Биография:
        Unicorns - это духи природы, а значит они священны для всего общества
        Elves. Они считаются тотемным животным всего Irollan, ибо предсказано,
        что когда последний Unicorn умрёт, погибнет и Irollan - Elven Kingdom,
        и все его жители тоже. Хотя правдивость этой легенды никому не дано
        узнать, тем не менее мерцающая аура Unicorns наделяет их умением
        прикрывать своих союзников от вражеских заклинаний.
    """
    def __init__(self):
        super().__init__("Unicorn",  # name
                         12,  # attack
                         12,  # protection
                         10,  # min_damage
                         20,  # max_damage
                         57,  # health
                         12,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         630,  # cost
                         270,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class FifthUpgraded(Unit):
    """
    Биография:
        Могучие союзники Elves, Silver Unicorns появляются из самого сердца
        леса, чтобы прогнать прочь любого захватчика. Их ясная аура защищает
        дружественных солдат от магии врага, а их блестящий рог может излучать
        слишком яркие вспышки света, которые могут на время ослеплять врагов.
    """
    def __init__(self):
        super().__init__("Silver Unicorn",  # name
                         17,  # attack
                         17,  # protection
                         10,  # min_damage
                         20,  # max_damage
                         77,  # health
                         12,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         900,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
