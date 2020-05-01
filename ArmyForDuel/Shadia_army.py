from ArmyGenerator.GenerateShadowLeague import Shadow
from Battle.army import Army
from Heroes.HeroCatalog.ShadowLeague.Shadiia import Witch

Shadiia_army = Shadow()
Shadiia_army.first_creature.add_count(Shadiia_army.first_creature, 100)
Shadiia_army.second_creature_upgraded.add_count(
    Shadiia_army.second_creature_upgraded, 100)
Shadiia_army.third_creature_upgraded.add_count(
    Shadiia_army.third_creature_upgraded, 64)
Shadiia_army.fourth_creature_upgraded.add_count(
    Shadiia_army.fourth_creature_upgraded, 32)
Shadiia_army.fifth_creature_upgraded.add_count(
    Shadiia_army.fifth_creature_upgraded, 16)
Shadiia_army.sixth_creature.add_count(Shadiia_army.sixth_creature, 4)
Shadiia_army.seventh_creature_upgraded.add_count(
    Shadiia_army.seventh_creature_upgraded, 1)

Shadiia_army = Army(
    Witch(),
    [
        Shadiia_army.first_creature,
        Shadiia_army.second_creature_upgraded,
        Shadiia_army.third_creature_upgraded,
        Shadiia_army.fourth_creature_upgraded,
        Shadiia_army.fifth_creature_upgraded,
        Shadiia_army.sixth_creature,
        Shadiia_army.seventh_creature_upgraded
    ]
)
