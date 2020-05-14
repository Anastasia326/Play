import pygame

from Battle.Field import Start_Battle
from Working_with_textures.Main_menu import create_window
from Working_with_textures.Window_singleton import window, fullscreen
from Working_with_textures.arrays import arrays_list, array_of_Forest, \
    array_of_Shadows, array_of_Mage, array_of_Inferno, array_of_Necro, \
    array_of_Orden, classes_list, opened_catalog, catalogs, hero_name, \
    heroes_list, modes
from Working_with_textures.choice_display import choose_class_display
from Working_with_textures.choose_mod import choose_mod
from Working_with_textures.information_menu import information_menu
from Working_with_textures.option_menu import option_menu
from Working_with_textures.show_hero import show_hero
from Working_with_textures.show_heroes import show_heroes
from Working_with_textures.show_unit import show_unit
from Working_with_textures.show_units import show_units
from Working_with_textures.was_clicked import button_was_clicked

pygame.init()

window.value, buttons_list = create_window(window.value, fullscreen.value)
run = True
page = "Main menu"
i = 0

while run:
    i += 1
    if i == 120000:
        run = False
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif page == "Main menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    ["Start Menu", "Options", "Information", None],
                    [mouse_x, mouse_y]
                )
                if was_clicked:
                    page = next_page
                    i = 0
                    if page == "Start Menu":
                        buttons_list = choose_mod(window.value,
                                                  fullscreen.value)
                    elif page == "Options":
                        buttons_list = option_menu(window.value,
                                                   fullscreen.value)
                    elif page == "Information":
                        buttons_list = information_menu(window.value,
                                                        fullscreen.value)
                    elif page is None:
                        run = False
                    else:
                        run = False
                        print("Look in main menu realization")
        elif page == "Options":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    ["800x600", "1178x663", "1280x720", "1920x1080",
                     "1600x800", "Fullscreen", "Return"],
                    [mouse_x, mouse_y]
                )
                if was_clicked:
                    page = "Options"
                    i = 0
                    if next_page == "Return":
                        page = "Main menu"
                        size = [pygame.display.get_surface().get_width(),
                                pygame.display.get_surface().get_height()]
                        window.value, buttons_list = create_window(
                            window.value,
                            fullscreen.value,
                            size[0], size[1])
                    elif next_page == "Fullscreen":
                        fullscreen.value = not fullscreen.value
                        buttons_list = option_menu(window.value,
                                                   fullscreen.value)
                    else:
                        create_window(window.value, fullscreen.value,
                                      int(next_page.split("x")[0]),
                                      int(next_page.split("x")[1]),
                                      False)
                        buttons_list = option_menu(window.value,
                                                   fullscreen.value)
        elif page == "Information":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    ["Heroes", "Units", "Main menu"],
                    [mouse_x, mouse_y]
                )
                if was_clicked:
                    page = next_page
                    i = 0
                    if page == "Main menu":
                        size = [pygame.display.get_surface().get_width(),
                                pygame.display.get_surface().get_height()]
                        window.value, buttons_list = create_window(
                            window.value,
                            fullscreen.value,
                            size[0], size[1])
                    elif page == "Heroes" or page == "Units":
                        buttons_list = choose_class_display(window.value,
                                                            fullscreen.value)
                    else:
                        run = False
                        print("look information page")
        elif page == "Start Menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    modes,
                    [mouse_x, mouse_y]
                )
                if next_page == "Return":
                    i = 0
                    page = "Main menu"
                    size = [pygame.display.get_surface().get_width(),
                            pygame.display.get_surface().get_height()]
                    window.value, buttons_list = create_window(
                        window.value,
                        fullscreen.value,
                        size[0],
                        size[1]
                    )
                else:
                    Start_Battle(window.value, fullscreen.value, next_page)
                    run = False

        elif page == "Units":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    classes_list + ["Information"],
                    [mouse_x, mouse_y]
                )
                if was_clicked:
                    page = next_page + " Units"
                    i = 0
                    if next_page in classes_list:
                        opened_catalog = catalogs[classes_list.index(
                            next_page)]
                        creatures_types = [
                            opened_catalog.FirstCreature.FirstNotUpgraded,
                            opened_catalog.SecondCreature.SecondNotUpgraded,
                            opened_catalog.ThirdCreature.ThirdNotUpgraded,
                            opened_catalog.FourthCreature.FourthNotUpgraded,
                            opened_catalog.FifthCreature.FifthNotUpgraded,
                            opened_catalog.SixthCreature.SixthNotUpgraded,
                            opened_catalog.SeventhCreature.SeventhNotUpgraded,
                            opened_catalog.FirstCreature.FirstUpgraded,
                            opened_catalog.SecondCreature.SecondUpgraded,
                            opened_catalog.ThirdCreature.ThirdUpgraded,
                            opened_catalog.FourthCreature.FourthUpgraded,
                            opened_catalog.FifthCreature.FifthUpgraded,
                            opened_catalog.SixthCreature.SixthUpgraded,
                            opened_catalog.SeventhCreature.SeventhUpgraded]
                        buttons_list, creatures_name = show_units(window.value,
                                                                  fullscreen.value,
                                                                  classes_list,
                                                                  arrays_list,
                                                                  next_page)
                    elif next_page == "Information":
                        page = "Information"
                        buttons_list = information_menu(window.value,
                                                        fullscreen.value)
                    else:
                        run = False
                        print("look Units page")
        elif page == "Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    classes_list + ["Information"],
                    [mouse_x, mouse_y]
                )
                if was_clicked:
                    if next_page == "Information":
                        buttons_list = information_menu(window.value,
                                                        fullscreen.value)
                        page = next_page
                        i = 0
                    else:
                        page = next_page + " Heroes"
                        i = 0
                        buttons_list, hero_name = show_heroes(window.value,
                                                              fullscreen.value,
                                                              next_page)
        elif page.split()[0] in classes_list and page.split()[1] == "Units":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    arrays_list[(classes_list.index(page.split()[0]))] + [
                        "Units"],
                    [mouse_x, mouse_y]
                )
                if was_clicked:
                    i = 0
                    if next_page in arrays_list[(classes_list.index(
                            page.split()[0]))]:
                        buttons_list = show_unit(window.value,
                                                 fullscreen.value,
                                                 opened_catalog,
                                                 catalogs,
                                                 arrays_list, creatures_types,
                                                 next_page)
                    elif next_page == "Units":
                        buttons_list = choose_class_display(window.value,
                                                            fullscreen.value)
                    else:
                        run = False
                        print("look Units page")
                    page = next_page
        elif page.split()[0] in classes_list and page.split()[1] == "Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    heroes_list[(classes_list.index(page.split()[0]))] + [
                        "Heroes"],
                    [mouse_x, mouse_y]
                )
                if was_clicked:
                    i = 0
                    if next_page in heroes_list[(classes_list.index(
                            page.split()[0]))]:
                        buttons_list = show_hero(window.value,
                                                 fullscreen.value,
                                                 hero_name[
                                                     hero_name.index(
                                                         next_page
                                                     )
                                                 ])
                    elif next_page == "Heroes":
                        buttons_list = choose_class_display(window.value,
                                                            fullscreen.value)
                    else:
                        run = False
                        print("look Heroes page")
                    page = next_page
                    i = 0

        else:
            for class_ in classes_list:
                if page in arrays_list[classes_list.index(class_)]:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pos = pygame.mouse.get_pos()
                        mouse_x, mouse_y = pos[0], pos[1]
                        if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                                buttons_list[0][2] and buttons_list[0][
                            1] < mouse_y \
                                < buttons_list[0][1] + buttons_list[0][3]:
                            i = 0
                            page = class_ + " Units"
                            buttons_list, creatures_name = show_units(
                                window.value,
                                fullscreen.value,
                                classes_list,
                                arrays_list,
                                class_)
                elif page in heroes_list[classes_list.index(class_)]:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pos = pygame.mouse.get_pos()
                        mouse_x, mouse_y = pos[0], pos[1]
                        if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                                buttons_list[0][2] and buttons_list[0][
                            1] < mouse_y \
                                < buttons_list[0][1] + buttons_list[0][3]:
                            i = 0
                            page = class_ + " Heroes"
                            buttons_list, creatures_name = show_heroes(
                                window.value,
                                fullscreen.value,
                                class_)

pygame.quit()
