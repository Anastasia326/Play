from Units.unit import Unit


class FirstNotUpgraded(Unit):
    """
    Биография:
        Pixies - это духи, хранящие Kersyls - гигантские деревья, на которых
        стоят города Sylvan. Они охраняют их и живут в ветвях этих гигантов,
        взамен получая кров и пищу. Эти существа не предназначены для войны, но
        они будут яростно защищать свой дом, если потребуется. Их стремительные
        атаки могут нанести урон более чем одному противнику, а их маленький
        размер и скорость делает невозможным ответный удар.
    """
    def __init__(self):
        super().__init__("Pixie",  # name
                         1,  # attack
                         1,  # protection
                         1,  # min_damage
                         2,  # max_damage
                         5,  # health
                         12,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         35,  # cost
                         20,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FirstUpgraded(Unit):
    """
    Биография:
        Sprites - это близкие родственники Pixies, которые живут на самых
        высоких ветвях гигантского дерева Kersyl. Их маленький размер и
        скорость позволяют им атаковать более чем одного врага, а затем
        отступить обратно без ответного удара со стороны атакованного. К тому
        же, их близость силам леса такова, что они могут призывать силы природы
        и применять их, как заклинания в битве.
    """
    def __init__(self):
        super().__init__("Sprite",  # name
                         2,  # attack
                         2,  # protection
                         2,  # min_damage
                         2,  # max_damage
                         6,  # health
                         15,  # initiative
                         7,  # speed
                         None,  # shots
                         10,  # mana
                         55,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
