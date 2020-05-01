from Spells.IncreasingSpell import IncreaseSpell


class SpellImmunity(IncreaseSpell):
    def __init__(self):
        super().__init__("Light",  # school
                         None,  # exceptions
                         {
                             "Advanced": "1-4 level spells",
                             "Expert": "all"
                         },  # effect
                         7,  # mana cost
                         4,  # level
                         1)  # Duration coef

    def increase(self) -> str:
        return "spell_immunity"
