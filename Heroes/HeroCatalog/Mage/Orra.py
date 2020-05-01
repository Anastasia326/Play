from Heroes.Hero_init import Hero


class Mage(Hero):
    def __init__(self):
        super().__init__("Orra",  # name
                         None,  # spells
                         0,  # attack
                         0,  # protection
                         0,  # morale
                         0,  # luck
                         2,  # witchcraft
                         3)  # knowledge
