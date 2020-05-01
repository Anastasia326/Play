from ArmyGenerator.GenerateNecropolis import necro
from Battle.army import Army
from Heroes.HeroCatalog.Nekro.Tiamovax import KnightOfDeath

Tiamovax_army = necro()
Tiamovax_army.first_creature.add_count(Tiamovax_army.first_creature, 100)
Tiamovax_army.second_creature_upgraded.add_count(
    Tiamovax_army.second_creature_upgraded, 100)
Tiamovax_army.third_creature_upgraded.add_count(
    Tiamovax_army.third_creature_upgraded, 64)
Tiamovax_army.fourth_creature_upgraded.add_count(
    Tiamovax_army.fourth_creature_upgraded, 32)
Tiamovax_army.fifth_creature_upgraded.add_count(
    Tiamovax_army.fifth_creature_upgraded, 16)
Tiamovax_army.sixth_creature.add_count(Tiamovax_army.sixth_creature, 4)
Tiamovax_army.seventh_creature_upgraded.add_count(
    Tiamovax_army.seventh_creature_upgraded, 1)

Tiamovax_army = Army(
    KnightOfDeath(),
    [
        Tiamovax_army.first_creature,
        Tiamovax_army.second_creature_upgraded,
        Tiamovax_army.third_creature_upgraded,
        Tiamovax_army.fourth_creature_upgraded,
        Tiamovax_army.fifth_creature_upgraded,
        Tiamovax_army.sixth_creature,
        Tiamovax_army.seventh_creature_upgraded
    ]
)
