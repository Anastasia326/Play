from Units.unit import Unit


class SecondNotUpgraded(Unit):
    """
    Биография:
         Blood Maidens - это молниеносные женщины-воины, которые используют
         искажённую форму Elven Battle Dance. Они двигаются быстро, чтобы
         напасть на своих противников, атаковать их и вернуться на своё
         стартовое место, и успевают сделать всё это за одно неуловимое
         действие.
    """
    def __init__(self):
        super().__init__("Blood Maiden",  # name
                         4,  # attack
                         2,  # protection
                         5,  # min_damage
                         7,  # max_damage
                         16,  # health
                         14,  # initiative
                         7,  # speed
                         None,  # shots
                         None,  # mana
                         125,  # cost
                         50,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)


class SecondUpgraded(Unit):
    """
    Биография:
         Blood Furies - это элитные солдаты армий Dark Elf. Они настолько
         хорошо обучены собственной вариации боевого стиля Battle Dance, что
         могут атаковать и ускользать от ответа в одной и той же атаке,
         предотвращая любую возможность врагов среагировать и ответить, перед
         тем как они отойдут.
    """
    def __init__(self):
        super().__init__("Blood Fury",  # name
                         5,  # attack
                         3,  # protection
                         5,  # min_damage
                         7,  # max_damage
                         16,  # health
                         16,  # initiative
                         8,  # speed
                         None,  # shots
                         None,  # mana
                         175,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
