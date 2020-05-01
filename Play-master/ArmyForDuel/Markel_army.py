from ArmyGenerator.GenerateNecropolis import necro
from Battle.army import Army
from Heroes.HeroCatalog.Nekro.Markel import Nekromant

Markel_army = necro()
Markel_army.first_creature.add_count(Markel_army.first_creature, 100)
Markel_army.second_creature_upgraded.add_count(
    Markel_army.second_creature_upgraded, 100)
Markel_army.third_creature_upgraded.add_count(
    Markel_army.third_creature_upgraded, 64)
Markel_army.fourth_creature_upgraded.add_count(
    Markel_army.fourth_creature_upgraded, 32)
Markel_army.fifth_creature_upgraded.add_count(
    Markel_army.fifth_creature_upgraded, 16)
Markel_army.sixth_creature.add_count(Markel_army.sixth_creature, 4)
Markel_army.seventh_creature_upgraded.add_count(
    Markel_army.seventh_creature_upgraded, 1)

Markel_army = Army(
    Nekromant(),
    [
        Markel_army.first_creature,
        Markel_army.second_creature_upgraded,
        Markel_army.third_creature_upgraded,
        Markel_army.fourth_creature_upgraded,
        Markel_army.fifth_creature_upgraded,
        Markel_army.sixth_creature,
        Markel_army.seventh_creature_upgraded
    ]
)
