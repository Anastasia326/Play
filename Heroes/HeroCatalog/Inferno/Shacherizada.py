from Heroes.Hero_init import Hero


class Heretic(Hero):
    def __init__(self):
        super().__init__("Shacherizada",  # name
                         None,  # spells
                         -2,  # attack
                         -3,  # protection
                         0,  # morale
                         2,  # luck
                         2,  # witchcraft
                         2)  # knowledge
