from ArmyGenerator.GenerateShadowLeague import Shadow
from Battle.army import Army
from Heroes.HeroCatalog.ShadowLeague.Railag import DarkElf

Railag_army = Shadow()
Railag_army.first_creature.add_count(Railag_army.first_creature, 157)
Railag_army.second_creature_upgraded.add_count(
    Railag_army.second_creature_upgraded, 134)
Railag_army.third_creature_upgraded.add_count(
    Railag_army.third_creature_upgraded, 155)
Railag_army.fourth_creature_upgraded.add_count(
    Railag_army.fourth_creature_upgraded, 13)
Railag_army.fifth_creature_upgraded.add_count(
    Railag_army.fifth_creature_upgraded, 124)
Railag_army.sixth_creature.add_count(Railag_army.sixth_creature, 5)
Railag_army.seventh_creature_upgraded.add_count(
    Railag_army.seventh_creature_upgraded, 9)

Railag_army = Army(
    DarkElf(),
    [
        Railag_army.first_creature,
        Railag_army.second_creature_upgraded,
        Railag_army.third_creature_upgraded,
        Railag_army.fourth_creature_upgraded,
        Railag_army.fifth_creature_upgraded,
        Railag_army.sixth_creature,
        Railag_army.seventh_creature_upgraded
    ]
)
