from Spells.IncreasingSpell import IncreaseSpell


class DeflectMissle(IncreaseSpell):
    def __init__(self):
        super().__init__("Light",  # school
                         None,  # exceptions
                         {
                             "None": "*0.75",
                             "Basic": "*0.60",
                             "Advanced": "*0.45",
                             "Expert": "*0.3"
                         },  # effect
                         6,  # mana cost
                         3,  # level
                         1)  # Duration coefficient

    def increase(self) -> str:
        return "damage_from_range"
