from Spells.DamageSpells import DamageSpell


class WordOFLight(DamageSpell):
    def __init__(self):
        super().__init__("Light",  # school
                         "Orden, Nature, Mage, Shadow",  # exceptions
                         None,  # effect
                         15,  # mana cost
                         5,  # level
                         12)  # Duration coef

    def deal_damage(self) -> int:
        return 144
