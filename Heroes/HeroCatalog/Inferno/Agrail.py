from Heroes.Hero_init import Hero


class Demon(Hero):
    def __init__(self):
        super().__init__(name = "Agrail",
                         spells = None,
                         attack = 2,
                         protection = 2,
                         morale = 0,
                         luck = 0,
                         witchcraft = 1,
                         knowledge = 1)
