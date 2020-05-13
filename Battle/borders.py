from ArmyForDuel.Agrail_army import Agrail_army
from ArmyForDuel.Faiidaen_army import Faiidaen_army
from ArmyForDuel.Ivanhoe_army import Ivanhoe_army
from ArmyForDuel.Legolas_army import Legolas_army
from ArmyForDuel.Markel_army import Markel_army
from ArmyForDuel.Orra_army import Orra_army
from ArmyForDuel.Railag_army import Railag_army
from ArmyForDuel.Shacherizada_army import Shacherizada_army
from ArmyForDuel.Shadia_army import Shadiia_army
from ArmyForDuel.Sverchok_army import Swerchok_army
from ArmyForDuel.Tiamovax_army import Tiamovax_army
from ArmyForDuel.Zexir_army import Zexir_army

borders = [[[0, 9], [0, 1]], [[0, 9], [10, 11]]]


def in_borders(coordinates, board=True, first_army_turn=True):
    if board:
        return 0 <= coordinates[0] <= 9 and 0 <= coordinates[1] <= 11
    elif first_army_turn:
        return 0 <= coordinates[0] <= 9 and 0 <= coordinates[1] <= 1
    else:
        return 0 <= coordinates[0] <= 9 and 10 <= coordinates[1] <= 11

units_of_swerchok = []
for solder in Swerchok_army.soldiers:
    units_of_swerchok += [solder.name]
units_of_Ivanhoe = []
for solder in Ivanhoe_army.soldiers:
    units_of_Ivanhoe += [solder.name]
units_of_Markel = []
for solder in Markel_army.soldiers:
    units_of_Markel += [solder.name]
units_of_Tiamovax = []
for solder in Tiamovax_army.soldiers:
    units_of_Tiamovax += [solder.name]
units_of_Agrail = []
for solder in Agrail_army.soldiers:
    units_of_Agrail += [solder.name]
units_of_Shacherizada = []
for solder in Shacherizada_army.soldiers:
    units_of_Shacherizada += [solder.name]
units_of_Faiidaen = []
for solder in Faiidaen_army.soldiers:
    units_of_Faiidaen += [solder.name]
units_of_Legolas = []
for solder in Legolas_army.soldiers:
    units_of_Legolas += [solder.name]
units_of_Railag = []
for solder in Railag_army.soldiers:
    units_of_Railag += [solder.name]
units_of_Shadiia = []
for solder in Shadiia_army.soldiers:
    units_of_Shadiia += [solder.name]
units_of_Orra = []
for solder in Orra_army.soldiers:
    units_of_Orra += [solder.name]
units_of_Zexir = []
for solder in Zexir_army.soldiers:
    units_of_Zexir += [solder.name]

army_list = [[Swerchok_army, Ivanhoe_army],
             [Markel_army, Tiamovax_army],
             [Agrail_army, Shacherizada_army],
             [Faiidaen_army, Legolas_army],
             [Railag_army, Shadiia_army],
             [Orra_army, Zexir_army]]
