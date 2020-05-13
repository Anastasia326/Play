from Heroes.Hero_init import Hero


class KnightOfDeath(Hero):
    def __init__(self):
        super().__init__(name="Tiamovax",
                         attack=1,
                         protection=2,
                         morale=0,
                         luck=0,
                         witchcraft=2,
                         knowledge=1)
