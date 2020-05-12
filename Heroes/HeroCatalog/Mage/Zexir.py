from Heroes.Hero_init import Hero


class Alchemist(Hero):
    def __init__(self):
        super().__init__(name = "Zexir",
                         spells = None,
                         attack = 1,
                         protection = 1,
                         morale = 0,
                         luck = 0,
                         witchcraft = 2,
                         knowledge = 2)
