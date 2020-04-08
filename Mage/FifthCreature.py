from Units.unit import Unit


class FifthNotUpgraded(Unit):
    """"
    Биография:
         Djinns - это древние духи стихий, которых Wizards могут призвать и
         магически привязать к себе. Таким образом, если Djinn привязан, он не
         может отступить, и будет защищать своего хозяина, пока его жизненные
         силы не оставят его. Djinns очень полезны на поле боя,
         но их магическая сущность делает их непредсказуемыми и
         неконтролируемыми. Невозможно предсказать, какое заклинание Djinn
         использует против врага, но в чём точно можно быть уверенным,
         так в том, что, как минимум, оно не повернётся против своих союзников.
         Умение колдовать не единственное их задание на поле боя, поскольку они
          могут участвовать в рукопашном бою, используя свою тяжёлую саблю.
    """
    def __init__(self):
        super().__init__("Djinn",  # name
                         11,  # attack
                         10,  # protection
                         12,  # min_damage
                         14,  # max_damage
                         40,  # health
                         12,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         460,  # cost
                         170,  # upgrade
                         2,  # length
                         2,  # width
                         {},  # spells
                         0)  # count)


class FifthUpgraded(Unit):
    """
    Биография:
         Djinn Sultans могут не только применять вредные заклинания против
         врагов, но также полезные заклинания на своих союзников. Однако, как и
        в ситуации с обычным Djinn, их заклинания совершенно непредсказуемы.
    """
    def __init__(self):
        super().__init__("Djinn Sultan",  # name
                         14,  # attack
                         14,  # protection
                         14,  # min_damage
                         19,  # max_damage
                         45,  # health
                         12,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         630,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         {},  # spells
                         0)  # count)
