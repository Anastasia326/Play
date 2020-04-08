from Units.unit import Unit


class FourthNotUpgraded(Unit):
    """
    Биография:
        Succubus создают сферы огня и кидают их во врагов. Любой атакующий
        солдат, должен быть готов к тому, что его встретит огненный дождь, если
         он сойдётся лицом к лицу с Succubus в битве.
    """
    def __init__(self):
        super().__init__("Succubus",  # name
                         6,  # attack
                         6,  # protection
                         6,  # min_damage
                         13,  # max_damage
                         20,  # health
                         10,  # initiative
                         4,  # speed
                         6,  # shots
                         None,  # mana
                         240,  # cost
                         110,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class FourthUpgraded(Unit):
    """
    Биография:
        Succubus Mistresses призывают сферы огня и обрушивают их на своих
        врагов. Это проклятое пламя не останавливается тогда, когда попадает в
        противника, вместо этого оно будет распространяться дальше, и скоро
        другие существа окажутся объятыми пламенем.
    """
    def __init__(self):
        super().__init__("Succubus Mistress",  # name
                         6,  # attack
                         6,  # protection
                         6,  # min_damage
                         13,  # max_damage
                         30,  # health
                         10,  # initiative
                         4,  # speed
                         6,  # shots
                         None,  # mana
                         350,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
