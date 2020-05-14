from ArmyGenerator.GenerateInferno import inferno
from Battle.army import Army
from Heroes.HeroCatalog.Inferno.Agrail import Demon

Agrail_army = inferno()
Agrail_army.first_creature_upgraded.add_count(
    Agrail_army.first_creature_upgraded, 123)
Agrail_army.second_creature_upgraded.add_count(
    Agrail_army.second_creature_upgraded, 188)
Agrail_army.third_creature_upgraded.add_count(
    Agrail_army.third_creature_upgraded, 31)
Agrail_army.fourth_creature_upgraded.add_count(
    Agrail_army.fourth_creature_upgraded, 15)
Agrail_army.fifth_creature_upgraded.add_count(
    Agrail_army.fifth_creature_upgraded, 16)
Agrail_army.sixth_creature.add_count(Agrail_army.sixth_creature, 4)
Agrail_army.seventh_creature_upgraded.add_count(
    Agrail_army.seventh_creature_upgraded, 2)

Agrail_army = Army(
    Demon(),
    [
        Agrail_army.first_creature,
        Agrail_army.second_creature_upgraded,
        Agrail_army.third_creature_upgraded,
        Agrail_army.fourth_creature_upgraded,
        Agrail_army.fifth_creature_upgraded,
        Agrail_army.sixth_creature,
        Agrail_army.seventh_creature_upgraded
    ]
)
