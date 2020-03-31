from Heroes.Hero_init import Hero


class Priest(Hero):
    def __init__(self):
        super().__init__("Swerchok",  # name
                         None,  # spells
                         1,  # attack
                         0,  # protection
                         0,  # morale
                         0,  # luck
                         2,  # witchcraft
                         2)  # knowledge
