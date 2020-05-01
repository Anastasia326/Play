from abc import ABC


class Spell(ABC):
    """
    Класс заклинание

    """
    def __init__(self, magic_school, exceptions, coefficient, mana_cost,
                 level, dur_coef):
        self.MagicSchool = magic_school
        self.exceptions = exceptions
        self.coefficient = coefficient
        self.mana_cost = mana_cost
        self.level = level
        self.duration_coef = dur_coef
