from ArmyGenerator.GenerateOrden import orden
from Battle.army import Army
from Heroes.HeroCatalog.Orden.Swerchok import Priest

Swerchok_army = orden()
Swerchok_army.first_creature.add_count(Swerchok_army.first_creature, 100)
Swerchok_army.second_creature_upgraded.add_count(
    Swerchok_army.second_creature_upgraded, 100)
Swerchok_army.third_creature_upgraded.add_count(
    Swerchok_army.third_creature_upgraded, 64)
Swerchok_army.fourth_creature_upgraded.add_count(
    Swerchok_army.fourth_creature_upgraded, 32)
Swerchok_army.fifth_creature_upgraded.add_count(
    Swerchok_army.fifth_creature_upgraded, 16)
Swerchok_army.sixth_creature.add_count(Swerchok_army.sixth_creature, 4)
Swerchok_army.seventh_creature_upgraded.add_count(
    Swerchok_army.seventh_creature_upgraded, 1)

Swerchok_army = Army(
    Priest(),
    [
        Swerchok_army.first_creature,
        Swerchok_army.second_creature_upgraded,
        Swerchok_army.third_creature_upgraded,
        Swerchok_army.fourth_creature_upgraded,
        Swerchok_army.fifth_creature_upgraded,
        Swerchok_army.sixth_creature,
        Swerchok_army.seventh_creature_upgraded
    ]
)
