from Spells.IncreasingSpell import IncreaseSpell


class DivineStrength(IncreaseSpell):
    def __init__(self):
        super().__init__("Light",  # school
                         None,  # exceptions
                         {
                             "None": "*0.5",
                             "Basic": "*0.65",
                             "Advanced": "*0.8",
                             "Expert": "*1"
                         },  # effect
                         4,  # mana cost
                         1,  # level
                         1)  # Duration coefficient

    def increase(self) -> str:
        return "min_damage"
