from Heroes.Hero_init import Hero


class Demon(Hero):
    def __init__(self):
        super().__init__("Agrail",  # name
                         None,  # spells
                         2,  # attack
                         2,  # protection
                         0,  # morale
                         0,  # luck
                         1,  # witchcraft
                         1)  # knowledge
