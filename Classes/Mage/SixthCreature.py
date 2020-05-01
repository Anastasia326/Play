from Units.unit import Unit


class SixthNotUpgraded(Unit):
    """
    Биография:
        Мстительные духи из забытых времён - Rakshasas, жили в наиболее
        отдалённых областях Ashan тысячелетиями. Жадные до мести, эту существа
        были найденны путешествующими Wizard, которые, после множества
        неудачных попыток, научились призывать и контролировать их.
        Rakshasa Rani - это внушительная сила на поле боя, наводящая страх на
        своих врагов своими мульти-вооружёнными, c головами львов телами и
        потрясающе наточенными мечами. Их атаки вселяют такой страх, что их
        враги даже не могут ответить на их атаку.
    """
    def __init__(self):
        super().__init__("Rakshasa Rani",  # name
                         25,  # attack
                         20,  # protection
                         15,  # min_damage
                         23,  # max_damage
                         120,  # health
                         9,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         1400,  # cost
                         300,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)


class SixthUpgraded(Unit):
    """
    Биография:
        Rakshasa Raja устрашает своих врагов точно так же, как и Rakshasa Rani,
        но в дополнение ко всему у них есть умение двигаться с увеличенной
        скоростью, когда это нужно.
    """
    def __init__(self):
        super().__init__("Rakshasa Raja",  # name
                         25,  # attack
                         20,  # protection
                         23,  # min_damage
                         30,  # max_damage
                         140,  # health
                         8,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         1700,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
