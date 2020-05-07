from Heroes.Hero_init import Hero


class Knight(Hero):
    def __init__(self):
        super().__init__(name = "Ivanhoe",
                         spells = None,
                         attack = 2,
                         protection = 2,
                         morale = 0,
                         luck = 0,
                         witchcraft = 1,
                         knowledge = 1)
