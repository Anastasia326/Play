from Heroes.Hero_init import Hero


class Druid(Hero):
    def __init__(self):
        super().__init__("Faidaen",  # name
                         None,  # spells
                         0,  # attack
                         2,  # protection
                         0,  # morale
                         0,  # luck
                         1,  # witchcraft
                         2)  # knowledge
