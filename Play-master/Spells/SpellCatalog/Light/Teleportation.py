from Spells.IncreasingSpell import IncreaseSpell


class Teleport(IncreaseSpell):
    def __init__(self):
        super().__init__("Light",  # school
                         None,  # exceptions
                         None,  # effect
                         8,  # mana cost
                         4,  # level
                         None)  # Duration coef

    def increase(self) -> str:
        return "move"
