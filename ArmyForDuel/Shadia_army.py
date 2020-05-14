from ArmyGenerator.GenerateShadowLeague import Shadow
from Battle.army import Army
from Heroes.HeroCatalog.ShadowLeague.Shadiia import Witch

Shadiia_army = Shadow()
Shadiia_army.first_creature.add_count(Shadiia_army.first_creature, 57)
Shadiia_army.second_creature_upgraded.add_count(
    Shadiia_army.second_creature_upgraded, 189)
Shadiia_army.third_creature_upgraded.add_count(
    Shadiia_army.third_creature_upgraded, 53)
Shadiia_army.fourth_creature_upgraded.add_count(
    Shadiia_army.fourth_creature_upgraded, 78)
Shadiia_army.fifth_creature_upgraded.add_count(
    Shadiia_army.fifth_creature_upgraded, 89)
Shadiia_army.sixth_creature.add_count(Shadiia_army.sixth_creature, 7)
Shadiia_army.seventh_creature.add_count(
    Shadiia_army.seventh_creature, 9)

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
