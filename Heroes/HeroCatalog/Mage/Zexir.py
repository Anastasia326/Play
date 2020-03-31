from Heroes.Hero_init import Hero


class Alchemist(Hero):
    def __init__(self):
        super().__init__("Orra",  # name
                         None,  # spells
                         1,  # attack
                         1,  # protection
                         0,  # morale
                         0,  # luck
                         2,  # witchcraft
                         2)  # knowledge
