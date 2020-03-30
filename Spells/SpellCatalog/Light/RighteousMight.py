from Spells.IncreasingSpell import IncreaseSpell


class Haste(IncreaseSpell):
    def __init__(self):
        super().__init__("Light",  # school
                         None,  # exceptions
                         {
                             "None": "+3",
                             "Basic": "+6",
                             "Advanced": "+9",
                             "Expert": "+12"
                         },  # effect
                         6,  # mana cost
                         3,  # level
                         1)  # Duration coef

    def increase(self) -> str:
        return "attack"
