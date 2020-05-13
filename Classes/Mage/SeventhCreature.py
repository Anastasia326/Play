from Units.unit import Unit


class SeventhNotUpgraded(Unit):
    """
    Биография:
        Colossus - наиболее могущественные существа, когда-либо созданные или
        призванные Wizards. Они создаются по такому же методу, как и Golems, но
        в ином масштабе. В каждом Colossus содержится частичка души его
        создателя. У него несгибаемая воля, что делает его иммунным к магии,
        контролирующей разум, что обеспечивает Wizards их неоспоримую
        лояльность. Не терпящие никакого оружия, Colossi используют в ближнем
        бою против своих оппонентов свои массивные руки и ноги.
    """
    def __init__(self):
        super().__init__("Colossus",  # name
                         27,  # attack
                         27,  # protection
                         40,  # min_damage
                         70,  # max_damage
                         175,  # health
                         10,  # initiative
                         6,  # speed
                         None,  # shots
                         None,  # mana
                         2700,  # cost
                         600,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = "Blue"


class SeventhUpgraded(Unit):
    """
    Биография:
        Создать Titan - это главный успех, о котором Wizard может мечтать. Как
        и Colossi, Titans необычайно смертельны, используя аналогично лишь
        голые руки, и также, как и Colossi имеют иммунитет к магии,
        контролирующей разум. Однако помимо этого, они ещё искусны в метании
        молний, а также в обрушивании разрядов молний на дальние дистанции.
    """
    def __init__(self):
        super().__init__("Titan",  # name
                         30,  # attack
                         30,  # protection
                         40,  # min_damage
                         70,  # max_damage
                         190,  # health
                         10,  # initiative
                         6,  # speed
                         5,  # shots
                         None,  # mana
                         3300,  # cost
                         None,  # upgrade
                         2,  # length
                         2,  # width
                         None,  # spells
                         0)  # count)
        self.special_resource = "Blue"
