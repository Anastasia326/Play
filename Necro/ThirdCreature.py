from random import randint

from Units.unit import Unit


class ThirdNotUpgraded(Unit):
    """
    Биография:
        Ghosts - это не обретшие покоя души мертвых, навечно привязанные к
        Necromancer, которые смогли подчинить их себе. Их тела бестелесны,
        что делает сложным нанести по ним удар.
    """
    def __init__(self):
        super().__init__("Ghost",  # name
                         5,  # attack
                         4,  # protection
                         2,  # min_damage
                         4,  # max_damage
                         16,  # health
                         10,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         100,  # cost
                         40,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count

    def get_damaged(self, damage) -> str:
        if randint(0, 100) < 50:
            return super().get_damaged(damage)


class ThirdUpgraded(Unit):
    """
    Биография:
        Spectres - это не обретшие покоя души мертвых, навечно привязанные к
        Necromancer, которые смогли подчинить их себе. Их тела бестелесны, что
        делает сложным нанести по ним удар. Прикосновение этих душ, сковывает и
        может высасывать ману вражеских существ, восстанавливая самих Spectres
        с помощью похищенной магии.
    """
    def __init__(self):
        super().__init__("Spectre",  # name
                         5,  # attack
                         4,  # protection
                         4,  # min_damage
                         6,  # max_damage
                         19,  # health
                         10,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         140,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)

    def get_damaged(self, damage) -> str:
        if randint(0, 100) < 40:
            return super().get_damaged(damage)
