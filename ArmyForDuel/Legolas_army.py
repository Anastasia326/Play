from ArmyGenerator.GenerateNature import Nature
from Battle.army import Army
from Heroes.HeroCatalog.NatureProtection.Legolas import Ranger

Legolas_army = Nature()
Legolas_army.first_creature.add_count(Legolas_army.first_creature, 100)
Legolas_army.second_creature_upgraded.add_count(
    Legolas_army.second_creature_upgraded, 100)
Legolas_army.third_creature_upgraded.add_count(
    Legolas_army.third_creature_upgraded, 64)
Legolas_army.fourth_creature_upgraded.add_count(
    Legolas_army.fourth_creature_upgraded, 32)
Legolas_army.fifth_creature_upgraded.add_count(
    Legolas_army.fifth_creature_upgraded, 16)
Legolas_army.sixth_creature.add_count(Legolas_army.sixth_creature, 4)
Legolas_army.seventh_creature_upgraded.add_count(
    Legolas_army.seventh_creature_upgraded, 1)

Legolas_army = Army(
    Ranger(),
    [
        Legolas_army.first_creature,
        Legolas_army.second_creature_upgraded,
        Legolas_army.third_creature_upgraded,
        Legolas_army.fourth_creature_upgraded,
        Legolas_army.fifth_creature_upgraded,
        Legolas_army.sixth_creature,
        Legolas_army.seventh_creature_upgraded
    ]
)
