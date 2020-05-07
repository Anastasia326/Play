from ArmyGenerator.GenerateInferno import inferno
from Battle.army import Army
from Heroes.HeroCatalog.Inferno.Shacherizada import Heretic

Shacherizada_army = inferno()
Shacherizada_army.first_creature.add_count(Shacherizada_army.first_creature, 100)
Shacherizada_army.second_creature_upgraded.add_count(
    Shacherizada_army.second_creature_upgraded, 100)
Shacherizada_army.third_creature_upgraded.add_count(
    Shacherizada_army.third_creature_upgraded, 64)
Shacherizada_army.fourth_creature_upgraded.add_count(
    Shacherizada_army.fourth_creature_upgraded, 32)
Shacherizada_army.fifth_creature_upgraded.add_count(
    Shacherizada_army.fifth_creature_upgraded, 16)
Shacherizada_army.sixth_creature.add_count(Shacherizada_army.sixth_creature, 4)
Shacherizada_army.seventh_creature_upgraded.add_count(
    Shacherizada_army.seventh_creature_upgraded, 1)

Shacherizada_army = Army(
    Heretic(),
    [
        Shacherizada_army.first_creature,
        Shacherizada_army.second_creature_upgraded,
        Shacherizada_army.third_creature_upgraded,
        Shacherizada_army.fourth_creature_upgraded,
        Shacherizada_army.fifth_creature_upgraded,
        Shacherizada_army.sixth_creature,
        Shacherizada_army.seventh_creature_upgraded
    ]
)
