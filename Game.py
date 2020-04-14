import os

import pygame

import Inferno
import Mage
import NatureProtection
import Necro
import Orden
import ShadowLeague
from Orden import FirstCreature, SecondCreature, ThirdCreature, \
    FourthCreature, FifthCreature, SixthCreature, SeventhCreature
from Working_with_textures.Main_menu import create_window
from Working_with_textures.choice_display import choose_class_display
from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size
from Working_with_textures.draw_button import draw_button
from Working_with_textures.draw_some_buttons import draw_some_buttons
from Working_with_textures.information_menu import information_menu
from Working_with_textures.option_menu import option_menu
from Working_with_textures.show_unit import show_unit
from Working_with_textures.show_units import show_units
from Working_with_textures.spell_menu import spell_menu
from Working_with_textures.start_menu import start_menu
from Working_with_textures.was_clicked import button_was_clicked

window = None
fullscreen = False


def show_heroes(class_name: str):
    """
    :param class_name: Witch class should be shown
    :return: buttons coordinates
    Create Hero menu
    """
    create_window_of_the_same_size(window, fullscreen)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    hero_list = []
    if class_name == "Orden":
        hero_list = ["Swerchok", "Ivanhoe"]
    elif class_name == "Necropolis":
        hero_list = ["Markel", "Tiamovax"]
    elif class_name == "Mage":
        hero_list = ["Orra", "Zexir"]
    elif class_name == "ShadowLeague":
        hero_list = ["Railag", "Shadia"]
    elif class_name == "NatureProtection":
        hero_list = ["Faidaen", "Legolas"]
    elif class_name == "Inferno":
        hero_list = ["Agrail", "Shacherizada"]
    else:
        print("Something went wrong. Please, tell Anastasia Kemova about that "
              "kemovakemova.aiu@phystech.edu (wrong classname)")
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 3,
                      width // 3,
                      length // 3,
                      width // 3))
    buttons = draw_some_buttons(window, 2, hero_list,
                                (length // 3,
                                 width // 3,
                                 length // 3,
                                 2 * width // 9))
    buttons += draw_some_buttons(window, 1, ["Return"],
                                 (length // 3,
                                  width // 3 - 30 + 2 * width // 9,
                                  length // 3,
                                  width // 9 + 15))
    pygame.display.update()
    return buttons


def show_hero(hero_name: str):
    """
    :param unit_name: what unit should be shown
    :return:
    """
    create_window_of_the_same_size(window, fullscreen)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    if os.name == "nt":
        background_image_of_unit = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + "заготовка.png")
    else:
        background_image_of_unit = pygame.image.load("заготовка.png")
    window.blit(background_image_of_unit, [0, 0])
    draw_button(window, (128, 0, 0),
                (length - 200, width - width // 10, 170, 100),
                "Return")
    if os.name == "nt":
        background_image_of_unit_face = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + hero_name + ".png")
    else:
        background_image_of_unit_face = pygame.image.load(hero_name + ".png")
    window.blit(background_image_of_unit_face, [40, 60])
    pygame.display.update()
    return [(length - 200, width - width // 10, 170, 100)]


pygame.init()

creatures_name = []
window, buttons_list = create_window(window, fullscreen)
run = True
array_of_Inferno = ["Imp", "Horned Demon", "Hell Hound", "Succubus",
                    "Hell Charger", "Pit Fiend", "Devil", "Familiar",
                    "Horned Overseer", "Cerberus", "Succubus Mistress",
                    "Nightmare", "Pit Lord", "Arch Devil"]
array_of_Orden = ["Villager", "Archer", "Footman", "Griffin", "Priest",
                  "Cavalier", "Angel", "Conscript", "Marksman", "Squire",
                  "Imperial Griffin", "Inquisitor", "Paladin", "Archangel"]
array_of_Necro = ["Skeleton", "Zombie", "Ghost", "Vampire", "Lich",
                  "Wight", "Bone Dragon", "Skeleton Archer", "Plague Zombie",
                  "Spectre", "Vampire Lord", "Archlich", "Wraith",
                  "Spectral Dragon"]
array_of_Forest = ["Pixie", "Blade Dancer", "Hunter", "Druid", "Unicorn",
                   "Treant", "Green Dragon", "Sprite", "War Dancer",
                   "Master Hunter", "Druid Elder", "Silver Unicorn",
                   "Ancien Treant", "Emerald Dragon"]
array_of_Shadows = ["Scout", "Blood Maiden", "Minotaur", "Dark Rider",
                    "Hydra", "Shadow Witch", "Shadow Dragon", "Assassin",
                    "Blood Fury", "Minotaur Guard", "Grim Rider", "Deep Hydra",
                    "Shadow Matriarch", "Black Dragon"]
array_of_Mage = ["Gremlin", "Stone Gargoyle", "Iron Golem", "Mage",
                 "Djinn", "Rakshasa Rani", "Colossus", "Master Gremlin",
                 "Obsidian Gargoyle", "Steel Golem", "Archmage",
                 "Djinn Sultan", "Rakshasa Raja", "Titan"]
classes_list = ["Orden", "Necropolis", "Inferno", "Mage", "ShadowLeague",
                "NatureProtection"]
catalogs = [Orden, Necro, Inferno, Mage, ShadowLeague, NatureProtection]
arrays_list = [array_of_Orden, array_of_Necro, array_of_Inferno,
               array_of_Mage, array_of_Shadows, array_of_Forest]
opened_catalog = Orden
creatures_types = [opened_catalog.FirstCreature.FirstNotUpgraded,
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
                        buttons_list = start_menu(window, fullscreen)
                    elif page == "Options":
                        buttons_list = option_menu(window, fullscreen)
                    elif page == "Information":
                        buttons_list = information_menu(window, fullscreen)
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
                        window, buttons_list = create_window(window,
                                                             fullscreen,
                                                             size[0], size[1])
                    elif next_page == "Fullscreen":
                        fullscreen = not fullscreen
                        buttons_list = option_menu(window, fullscreen)
                    else:
                        create_window(window, fullscreen,
                                      int(next_page.split("x")[0]),
                                      int(next_page.split("x")[1]),
                                      False)
                        buttons_list = option_menu(window, fullscreen)
        elif page == "Information":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    ["Heroes", "Spells", "Units", "Main menu"],
                    [mouse_x, mouse_y]
                )
                if was_clicked:
                    page = next_page
                    i = 0
                    if page == "Main menu":
                        size = [pygame.display.get_surface().get_width(),
                                pygame.display.get_surface().get_height()]
                        window, buttons_list = create_window(window,
                                                             fullscreen,
                                                             size[0], size[1])
                    elif page == "Spells":
                        buttons_list = spell_menu(window, fullscreen)
                    elif page == "Heroes" or page == "Units":
                        buttons_list = choose_class_display(window, fullscreen)
                    else:
                        run = False
                        print("look information page")
        elif page == "Start Menu":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Main menu"
                    size = [pygame.display.get_surface().get_width(),
                            pygame.display.get_surface().get_height()]
                    window, buttons_list = create_window(window, fullscreen,
                                                         size[0], size[1])
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
                        buttons_list, creatures_name = show_units(window,
                                                                  fullscreen,
                                                                  classes_list,
                                                                  arrays_list,
                                                                  next_page)
                    elif next_page == "Information":
                        page = "Information"
                        buttons_list = information_menu(window, fullscreen)
                    else:
                        run = False
                        print("look Units page")
        elif page == "Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Orden Heroes"
                    buttons_list = show_heroes("Orden")
                elif buttons_list[1][0] < mouse_x < buttons_list[1][0] + \
                        buttons_list[1][2] and buttons_list[1][1] < mouse_y \
                        < buttons_list[1][1] + buttons_list[1][3]:
                    i = 0
                    page = "Necropolis Heroes"
                    buttons_list = show_heroes("Necropolis")
                elif buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Inferno Heroes"
                    buttons_list = show_heroes("Inferno")
                elif buttons_list[3][0] < mouse_x < buttons_list[3][0] + \
                        buttons_list[3][2] and buttons_list[3][1] < mouse_y \
                        < buttons_list[3][1] + buttons_list[3][3]:
                    page = "NatureProtection Heroes"
                    buttons_list = show_heroes("NatureProtection")
                    i = 0
                elif buttons_list[4][0] < mouse_x < buttons_list[4][0] + \
                        buttons_list[4][2] and buttons_list[4][1] < mouse_y \
                        < buttons_list[4][1] + buttons_list[4][3]:
                    page = "ShadowLeague Heroes"
                    buttons_list = show_heroes("ShadowLeague")
                    i = 0
                elif buttons_list[5][0] < mouse_x < buttons_list[5][0] + \
                        buttons_list[5][2] and buttons_list[5][1] < mouse_y \
                        < buttons_list[5][1] + buttons_list[5][3]:
                    page = "Mage Heroes"
                    buttons_list = show_heroes("Mage")
                    i = 0
                elif buttons_list[6][0] < mouse_x < buttons_list[6][0] + \
                        buttons_list[6][2] and buttons_list[6][1] < mouse_y \
                        < buttons_list[6][1] + buttons_list[6][3]:
                    page = "Information"
                    buttons_list = information_menu(window, fullscreen)
                    i = 0
        elif page == "Spells":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    ["Dark", "Destructive", "Light", "Summoning",
                     "Information"],
                    [mouse_x, mouse_y]
                )
                if was_clicked:
                    page = next_page
                    i = 0
                    if next_page == "Dark":
                        buttons_list = start_menu(window, fullscreen)
                    elif next_page == "Destructive":
                        buttons_list = start_menu(window, fullscreen)
                    elif next_page == "Light":
                        buttons_list = start_menu(window, fullscreen)
                    elif next_page == "Summoning":
                        buttons_list = start_menu(window, fullscreen)
                    elif next_page == "Information":
                        buttons_list = information_menu(window, fullscreen)
                    else:
                        run = False
                        print("look Spells page")
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
                        buttons_list = show_unit(window, fullscreen,
                                                 opened_catalog,
                                                 array_of_Orden,
                                                 array_of_Necro, array_of_Mage,
                                                 array_of_Forest,
                                                 array_of_Inferno,
                                                 array_of_Shadows, catalogs,
                                                 arrays_list, creatures_types,
                                                 next_page)
                    elif next_page == "Units":
                        buttons_list = choose_class_display(window, fullscreen)
                    else:
                        run = False
                        print("look Units page")
                    page = next_page
        elif page == "Orden Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Heroes"
                    buttons_list = choose_class_display(window, fullscreen)
                else:
                    for index in range(2):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[index][
                            3]:
                            i = 0
                            page = creatures_name[index]
                            buttons_list = show_hero(creatures_name[index])
                            break
        elif page == "Necropolis Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Heroes"
                    buttons_list = choose_class_display(window, fullscreen)
                else:
                    for index in range(2):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[index][
                            3]:
                            i = 0
                            page = creatures_name[index]
                            buttons_list = show_hero(creatures_name[index])
                            break
        elif page == "NatureProtection Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Heroes"
                    buttons_list = choose_class_display(window, fullscreen)
                else:
                    for index in range(2):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[index][
                            3]:
                            i = 0
                            page = creatures_name[index]
                            buttons_list = show_hero(creatures_name[index])
                            break
        elif page == "ShadowLeague Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Heroes"
                    buttons_list = choose_class_display(window, fullscreen)
                else:
                    for index in range(2):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[index][
                            3]:
                            i = 0
                            page = creatures_name[index]
                            buttons_list = show_hero(creatures_name[index])
                            break
        elif page == "Inferno Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Heroes"
                    buttons_list = choose_class_display(window, fullscreen)
                else:
                    for index in range(2):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[index][
                            3]:
                            i = 0
                            page = creatures_name[index]
                            buttons_list = show_hero(creatures_name[index])
                            break
        elif page == "Mage Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Heroes"
                    buttons_list = choose_class_display(window, fullscreen)
                else:
                    for index in range(2):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[index][
                            3]:
                            i = 0
                            page = creatures_name[index]
                            buttons_list = show_hero(creatures_name[index])
                            break
        elif page in array_of_Inferno:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Inferno Units"
                    buttons_list, creatures_name = show_units(window,
                                                              fullscreen,
                                                              classes_list,
                                                              arrays_list,
                                                              "Inferno")
        elif page in array_of_Forest:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "NatureProtection Units"
                    buttons_list, creatures_name = show_units(window,
                                                              fullscreen,
                                                              classes_list,
                                                              arrays_list,
                                                              "Nature"
                                                              "Protection")
        elif page in array_of_Mage:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Mage Units"
                    buttons_list, creatures_name = show_units(window,
                                                              fullscreen,
                                                              classes_list,
                                                              arrays_list,
                                                              "Mage")
        elif page in array_of_Necro:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Necropolis Units"
                    buttons_list, creatures_name = show_units(window,
                                                              fullscreen,
                                                              classes_list,
                                                              arrays_list,
                                                              "Necropolis")
        elif page in array_of_Shadows:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "ShadowLeague Units"
                    buttons_list, creatures_name = show_units(window,
                                                              fullscreen,
                                                              classes_list,
                                                              arrays_list,
                                                              "ShadowLeague")
        elif page in array_of_Orden:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Orden Units"
                    buttons_list, creatures_name = show_units(window,
                                                              fullscreen,
                                                              classes_list,
                                                              arrays_list,
                                                              "Orden")
        elif page == "Agrail":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Inferno Heroes"
                    buttons_list, creatures_name = show_heroes("Inferno")
        elif page == "Shacherizada":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Inferno Heroes"
                    buttons_list, creatures_name = show_heroes("Inferno")
        elif page == "Zexir":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Mage Heroes"
                    buttons_list, creatures_name = show_heroes("Mage")
        elif page == "Orra":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Mage Heroes"
                    buttons_list, creatures_name = show_heroes("Mage")
        elif page == "Legolas":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "NatureProtection Heroes"
                    buttons_list, creatures_name = show_heroes(
                        "NatureProtection")
        elif page == "Faidaen":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "NatureProtection Heroes"
                    buttons_list, creatures_name = show_heroes(
                        "NatureProtection")
        elif page == "Tiamovax":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Necropolis Heroes"
                    buttons_list, creatures_name = show_heroes("Necropolis")
        elif page == "Markel":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Necropolis Heroes"
                    buttons_list, creatures_name = show_heroes("Necropolis")
        elif page == "Shadiia":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "ShadowLeague Heroes"
                    buttons_list, creatures_name = show_heroes("ShadowLeague")
        elif page == "Railag":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "ShadowLeague Heroes"
                    buttons_list, creatures_name = show_heroes("ShadowLeague")
        elif page == "Ivanhoe":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Orden Heroes"
                    buttons_list, creatures_name = show_heroes("Orden")
        elif page == "Swerchok":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Orden Heroes"
                    buttons_list, creatures_name = show_heroes("Orden")
        else:
            print("Something went wrong. "
                  "Please, tell Anastasia Kemova about that kemova"
                  "kemova.aiu@phystech.edu\n"
                  "say that page is", page)
            run = False

pygame.quit()
