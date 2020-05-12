from Heroes.Hero_init import Hero


class Ranger(Hero):
    def __init__(self):
        super().__init__(name = "Legolas",
                         spells = None,
                         attack = 1,
                         protection = 3,
                         morale = 0,
                         luck = 0,
                         witchcraft = 1,
                         knowledge = 1)
