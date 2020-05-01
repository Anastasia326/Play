from ArmyGenerator.GenerateOrden import orden
from Battle.army import Army
from Heroes.HeroCatalog.Orden.Ivanhoe import Knight

Ivanhoe_army = orden()
Ivanhoe_army.first_creature.add_count(Ivanhoe_army.first_creature, 100)
Ivanhoe_army.second_creature_upgraded.add_count(
    Ivanhoe_army.second_creature_upgraded, 100)
Ivanhoe_army.third_creature_upgraded.add_count(
    Ivanhoe_army.third_creature_upgraded, 64)
Ivanhoe_army.fourth_creature_upgraded.add_count(
    Ivanhoe_army.fourth_creature_upgraded, 32)
Ivanhoe_army.fifth_creature_upgraded.add_count(
    Ivanhoe_army.fifth_creature_upgraded, 16)
Ivanhoe_army.sixth_creature.add_count(Ivanhoe_army.sixth_creature, 4)
Ivanhoe_army.seventh_creature_upgraded.add_count(
    Ivanhoe_army.seventh_creature_upgraded, 1)

Ivanhoe_army = Army(
    Knight(),
    [
        Ivanhoe_army.first_creature,
        Ivanhoe_army.second_creature_upgraded,
        Ivanhoe_army.third_creature_upgraded,
        Ivanhoe_army.fourth_creature_upgraded,
        Ivanhoe_army.fifth_creature_upgraded,
        Ivanhoe_army.sixth_creature,
        Ivanhoe_army.seventh_creature_upgraded
    ]
)
