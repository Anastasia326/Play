from ArmyGenerator.GenerateInferno import inferno
from Battle.army import Army
from Heroes.HeroCatalog.Inferno.Agrail import Demon

Agrail_army = inferno()
Agrail_army.first_creature.add_count(Agrail_army.first_creature, 100)
Agrail_army.second_creature_upgraded.add_count(
    Agrail_army.second_creature_upgraded, 100)
Agrail_army.third_creature_upgraded.add_count(
    Agrail_army.third_creature_upgraded, 64)
Agrail_army.fourth_creature_upgraded.add_count(
    Agrail_army.fourth_creature_upgraded, 32)
Agrail_army.fifth_creature_upgraded.add_count(
    Agrail_army.fifth_creature_upgraded, 16)
Agrail_army.sixth_creature.add_count(Agrail_army.sixth_creature, 4)
Agrail_army.seventh_creature_upgraded.add_count(
    Agrail_army.seventh_creature_upgraded, 1)

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
