from ArmyGenerator.GenerateMage import mage
from Battle.army import Army
from Heroes.HeroCatalog.Mage.Zexir import Alchemist

Zexir_army = mage()
Zexir_army.first_creature.add_count(Zexir_army.first_creature, 100)
Zexir_army.second_creature_upgraded.add_count(
    Zexir_army.second_creature_upgraded, 100)
Zexir_army.third_creature_upgraded.add_count(
    Zexir_army.third_creature_upgraded, 64)
Zexir_army.fourth_creature_upgraded.add_count(
    Zexir_army.fourth_creature_upgraded, 32)
Zexir_army.fifth_creature_upgraded.add_count(
    Zexir_army.fifth_creature_upgraded, 16)
Zexir_army.sixth_creature.add_count(Zexir_army.sixth_creature, 4)
Zexir_army.seventh_creature_upgraded.add_count(
    Zexir_army.seventh_creature_upgraded, 1)

Zexir_army = Army(
    Alchemist(),
    [
        Zexir_army.first_creature,
        Zexir_army.second_creature_upgraded,
        Zexir_army.third_creature_upgraded,
        Zexir_army.fourth_creature_upgraded,
        Zexir_army.fifth_creature_upgraded,
        Zexir_army.sixth_creature,
        Zexir_army.seventh_creature_upgraded
    ]
)
