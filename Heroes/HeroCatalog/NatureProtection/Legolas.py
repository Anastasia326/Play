from Heroes.Hero_init import Hero


class Ranger(Hero):
    def __init__(self):
        super().__init__("Legolas",  # name
                         None,  # spells
                         1,  # attack
                         3,  # protection
                         0,  # morale
                         0,  # luck
                         1,  # witchcraft
                         1)  # knowledge
