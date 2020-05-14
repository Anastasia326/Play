from ArmyGenerator.GenerateMage import mage
from Battle.army import Army
from Heroes.HeroCatalog.Mage.Orra import Mage

Orra_army = mage()
Orra_army.first_creature.add_count(Orra_army.first_creature, 153)
Orra_army.second_creature_upgraded.add_count(
    Orra_army.second_creature_upgraded, 164)
Orra_army.third_creature_upgraded.add_count(
    Orra_army.third_creature_upgraded, 67)
Orra_army.fourth_creature_upgraded.add_count(
    Orra_army.fourth_creature_upgraded, 97)
Orra_army.fifth_creature_upgraded.add_count(
    Orra_army.fifth_creature_upgraded, 16)
Orra_army.sixth_creature.add_count(Orra_army.sixth_creature, 5)
Orra_army.seventh_creature_upgraded.add_count(
    Orra_army.seventh_creature_upgraded, 3)

Orra_army = Army(
    Mage(),
    [
        Orra_army.first_creature,
        Orra_army.second_creature_upgraded,
        Orra_army.third_creature_upgraded,
        Orra_army.fourth_creature_upgraded,
        Orra_army.fifth_creature_upgraded,
        Orra_army.sixth_creature,
        Orra_army.seventh_creature_upgraded
    ]
)
