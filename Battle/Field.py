import pygame

from Working_with_textures.chose_with_whom_play import chose_with_whom_play
from Working_with_textures.window_with_choise import create_window_choise
from Working_with_textures.was_clicked import button_was_clicked
from Working_with_textures.NewField import create_window_of_Field
from Battle.Battle_ import Battle
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
from Working_with_textures.arrays import heroes_list, classes_list


def Start_Battle(window, fullscreen):
    run = True
    buttons_list = []
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

    What_happened = "Choise"
    window = create_window_of_Field(window, fullscreen, "Field")
    pygame.draw.line(window, (90, 90, 255), (10, 100), (20, 50))
    i = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    a = True
    start = 0
    first_army = None
    second_army = None
    while run:
        pygame.time.delay(1)
        i += 1
        if i == 120000:
            run = False
        x = 10
        clock = pygame.time.Clock()
        while x <= 840 and a == True:
            font = pygame.font.SysFont('dejavuserif', 60)
            text = font.render("Let the battle begin!", True, (255, 215, 0))
            clock.tick(60)
            window = create_window_of_Field(window, fullscreen, "Field")
            window.blit(text, (x, 250))
            x += 30
            pygame.display.update()
        a = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if What_happened == "Choise":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    was_clicked, buttons_list = create_window_choise(window,
                                                                     fullscreen)
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(buttons_list,
                                                                ["Orden",
                                                                 "Necropolis",
                                                                 "Inferno",
                                                                 "NatureProtection",
                                                                 "ShadowLeague",
                                                                 "Mage"],
                                                                [mouse_x,
                                                                 mouse_y])
                    if next_page is not None:
                        What_happened = next_page
                        index_ = classes_list.index(What_happened)
                        buttons_list = chose_with_whom_play(
                            window,
                            fullscreen,
                            heroes_list[index_][0],
                            heroes_list[index_][1]
                        )

                    print(next_page, What_happened)
            elif What_happened == "Orden":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(
                        buttons_list,
                        ["Ivanhoe", "Swerchok"],
                        [mouse_x, mouse_y]
                    )
                    start += 1
                    if start == 1:
                        What_happened = "Choise"
                        if next_page == "Ivanhoe":
                            first_army = Ivanhoe_army
                        elif next_page == "Swerchok":
                            first_army = Swerchok_army
                    if was_clicked and start == 2:
                        if next_page == "Ivanhoe":
                            second_army = Ivanhoe_army
                        elif next_page == "Swerchok":
                            second_army = Swerchok_army
                        What_happened = "Set up the army"
            elif What_happened == "Necropolis":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(
                        buttons_list,
                        ["Markel", "Tiamovax"],
                        [mouse_x, mouse_y]
                    )
                    start += 1
                    if start == 1:
                        What_happened = "Choise"
                        if next_page == "Markel":
                            first_army = Markel_army
                        elif next_page == "Tiamovax":
                            first_army = Tiamovax_army
                    if was_clicked and start == 2:
                        if next_page == "Markel":
                            second_army = Markel_army
                        elif next_page == "Tiamovax":
                            second_army = Tiamovax_army
                        What_happened = "Set up the army"
            elif What_happened == "Inferno":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(
                        buttons_list,
                        ["Agrail", "Shacherizada"],
                        [mouse_x, mouse_y]
                    )
                    start += 1
                    if start == 1:
                        What_happened = "Choise"
                        if next_page == "Agrail":
                            first_army = Agrail_army
                        elif next_page == "Shacherizada":
                            first_army = Shacherizada_army
                    if was_clicked and start == 2:
                        if next_page == "Agrail":
                            second_army = Agrail_army
                        elif next_page == "Shacherizada":
                            second_army = Shacherizada_army
                        What_happened = "Set up the army"
            elif What_happened == "NatureProtection":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(
                        buttons_list,
                        ["Faidaen", "Legolas"],
                        [mouse_x, mouse_y]
                    )
                    start += 1
                    if start == 1:
                        What_happened = "Choise"
                        if next_page == "Faidaen":
                            first_army = Faiidaen_army
                        elif next_page == "Legolas":
                            first_army = Legolas_army
                    if was_clicked and start == 2:
                        if next_page == "Faidaen":
                            second_army = Faiidaen_army
                        elif next_page == "Legolas":
                            second_army = Legolas_army
                        What_happened = "Set up the army"
            elif What_happened == "ShadowLeague":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(
                        buttons_list,
                        ["Railag", "Shadiia"],
                        [mouse_x, mouse_y]
                    )
                    start += 1
                    if start == 1:
                        What_happened = "Choise"
                        if next_page == "Railag":
                            first_army = Railag_army
                        elif next_page == "Shadiia":
                            first_army = Shadiia_army
                    if was_clicked and start == 2:
                        if next_page == "Railag":
                            second_army = Railag_army
                        elif next_page == "Shadiia":
                            second_army = Shadiia_army
                        What_happened = "Set up the army"
            elif What_happened == "Mage":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(
                        buttons_list,
                        ["Orra", "Zexir"],
                        [mouse_x, mouse_y]
                    )
                    start += 1
                    if start == 1:
                        What_happened = "Choise"
                        if next_page == "Orra":
                            first_army = Orra_army
                        elif next_page == "Zexir":
                            first_army = Zexir_army
                    if was_clicked and start == 2:
                        if next_page == "Orra":
                            second_army = Orra_army
                        elif next_page == "Zexir":
                            second_army = Zexir_army
                        What_happened = "Set up the army"

            elif What_happened == "Set up the army":
                battle = Battle(first_army, second_army, window, fullscreen)
                battle.battle()
                What_happened = "End"
            elif What_happened == "End":
                buttons_list = end_of_game(window, fullscreen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(
                        buttons_list, ["Exit"], [mouse_x, mouse_y])
                    if was_clicked:
                        What_happened = next_page
            elif What_happened == "Exit":
                run = False
