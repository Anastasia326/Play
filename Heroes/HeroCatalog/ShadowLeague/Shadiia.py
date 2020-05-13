from Heroes.Hero_init import Hero


class Witch(Hero):
    def __init__(self):
        super().__init__(name="Shadia",
                         attack=1,
                         protection=0,
                         morale=0,
                         luck=0,
                         witchcraft=2,
                         knowledge=2)
