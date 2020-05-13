from Heroes.Hero_init import Hero


class Mage(Hero):
    def __init__(self):
        super().__init__(name="Orra",
                         attack=0,
                         protection=0,
                         morale=0,
                         luck=0,
                         witchcraft=2,
                         knowledge=3)
