from Units.unit import Unit


class ThirdNotUpgraded(Unit):
    """
    Биография:
        Также как и другие Beastmen, Minotaurs - на половину люди и на
        половину быки, были созданы в результате экспериментов Wizards из
        Seven Silver Cities, как замена неконтролируемым Orcs. Но они сбежали
        на восток, под землю, в надежде найти там свободу, однако немногим
        позже были завоёваны армиями Dark Elves и были закованы в цепи и одеты
        в намордники. В обществе Dark Elf, Minotaurs используются как слуги и
        рабы, чтобы выполнять наиболее унизительные и тяжёлые задания.
        Несмотря на такое к ним отношение, Minotaurs известны своей
        храбростью и чувством собственного достоинства. Они выполнят любое
        задание на пределе своих возможностей, даже для тех, кто относится
        к ним, как к жалким рабам. Они также мечтают однажды обрести свободу,
        а Dark Elves опасаются того, что однажды, они будут сами взяты в
        рабство взамен.
    """
    def __init__(self):
        super().__init__("Minotaur",  # name
                         5,  # attack
                         2,  # protection
                         4,  # min_damage
                         7,  # max_damage
                         31,  # health
                         8,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         140,  # cost
                         60,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count


class ThirdUpgraded(Unit):
    """
    Биография:
         Величайшие из бойцов Minotaur получают дополнительное гладиаторское
         обучение, и награждаются званием Guard Minotaur. На них наносят
         татуировки, являющиеся эмблемами того поста, который этот Minotaur
         занимает. Они также профессионально используют смертельный
         двухсторонний топор, нанося последовательно два серьезных удара.
    """
    def __init__(self):
        super().__init__("Minotaur Guard",  # name
                         5,  # attack
                         2,  # protection
                         4,  # min_damage
                         7,  # max_damage
                         35,  # health
                         8,  # initiative
                         5,  # speed
                         None,  # shots
                         None,  # mana
                         200,  # cost
                         None,  # upgrade
                         1,  # length
                         1,  # width
                         None,  # spells
                         0)  # count)
