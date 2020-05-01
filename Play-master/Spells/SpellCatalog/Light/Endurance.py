from Spells.IncreasingSpell import IncreaseSpell


class Endurance(IncreaseSpell):
    def __init__(self):
        super().__init__("Light",  # school
                         None,  # exceptions
                         {
                             "None": "+3",
                             "Basic": "+6",
                             "Advanced": "+9",
                             "Expert": "+12"
                         },  # effect
                         4,  # mana cost
                         2,  # level
                         1)  # Duration coefficient

    def increase(self) -> str:
        return "defense"
