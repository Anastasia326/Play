from ArmyGenerator.GenerateNature import Nature
from Battle.army import Army
from Heroes.HeroCatalog.NatureProtection.Faidaen import Druid

Faiidaen_army = Nature()
Faiidaen_army.first_creature.add_count(Faiidaen_army.first_creature, 100)
Faiidaen_army.second_creature_upgraded.add_count(
    Faiidaen_army.second_creature_upgraded, 100)
Faiidaen_army.third_creature_upgraded.add_count(
    Faiidaen_army.third_creature_upgraded, 64)
Faiidaen_army.fourth_creature.add_count(
    Faiidaen_army.fourth_creature, 32)
Faiidaen_army.fifth_creature_upgraded.add_count(
    Faiidaen_army.fifth_creature_upgraded, 16)
Faiidaen_army.sixth_creature.add_count(Faiidaen_army.sixth_creature, 4)
Faiidaen_army.seventh_creature_upgraded.add_count(
    Faiidaen_army.seventh_creature_upgraded, 1)

Faiidaen_army = Army(
    Druid(),
    [
        Faiidaen_army.first_creature,
        Faiidaen_army.second_creature_upgraded,
        Faiidaen_army.third_creature_upgraded,
        Faiidaen_army.fourth_creature_upgraded,
        Faiidaen_army.fifth_creature_upgraded,
        Faiidaen_army.sixth_creature,
        Faiidaen_army.seventh_creature_upgraded
    ]
)
