from Heroes.Hero_init import Hero


class Druid(Hero):
    def __init__(self):
        super().__init__(name="Faidaen",
                         attack=0,
                         protection=2,
                         morale=0,
                         luck=0,
                         witchcraft=1,
                         knowledge=2)
