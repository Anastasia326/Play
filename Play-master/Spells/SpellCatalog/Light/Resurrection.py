from Spells.HealingSpell import HealingSpell


class Resurrection(HealingSpell):
    def __init__(self):
        super().__init__("Light",  # school
                         None,  # exceptions
                         "240",  # effect
                         6,  # mana cost
                         3,  # level
                         30)  # Duration coef

    def increase(self) -> str:
        return "Health"
