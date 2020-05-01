from Spells.IncreasingSpell import IncreaseSpell


class Haste(IncreaseSpell):
    def __init__(self):
        super().__init__("Light",  # school
                         None,  # exceptions
                         {
                             "None": "*1.1",
                             "Basic": "*1.2",
                             "Advanced": "*1.3",
                             "Expert": "*1.4"
                         },  # effect
                         4,  # mana cost
                         1,  # level
                         1)  # Duration coefficient

    def increase(self) -> str:
        return "speed"
