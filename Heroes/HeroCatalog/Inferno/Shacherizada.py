from Heroes.Hero_init import Hero


class Heretic(Hero):
    def __init__(self):
        super().__init__(name="Shacherizada",
                         spells=None,
                         attack=0,
                         protection=2,
                         morale=1,
                         luck=2,
                         witchcraft=2,
                         knowledge=2)
