from Heroes.Hero_init import Hero


class Heretic(Hero):
    def __init__(self):
        super().__init__("Shacherizada",  # name
                         None,  # spells
                         0,  # attack
                         2,  # protection
                         1,  # morale
                         2,  # luck
                         2,  # witchcraft
                         2)  # knowledge
