from Heroes.Hero_init import Hero


class KnightOfDeath(Hero):
    def __init__(self):
        super().__init__("Faidaen",  # name
                         None,  # spells
                         1,  # attack
                         2,  # protection
                         0,  # morale
                         0,  # luck
                         2,  # witchcraft
                         1)  # knowledge
