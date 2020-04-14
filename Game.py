import ctypes
import os

import pygame
from screeninfo import get_monitors

import Orden
import Necro
import NatureProtection
import ShadowLeague
import Inferno
import Mage

from Orden import FirstCreature, SecondCreature, ThirdCreature, \
    FourthCreature, FifthCreature, SixthCreature, SeventhCreature
from Necro import FirstCreature, SecondCreature, ThirdCreature, \
    FourthCreature, FifthCreature, SixthCreature, SeventhCreature
from NatureProtection import FirstCreature, SecondCreature, ThirdCreature, \
    FourthCreature, FifthCreature, SixthCreature, SeventhCreature
from ShadowLeague import FirstCreature, SecondCreature, ThirdCreature, \
    FourthCreature, FifthCreature, SixthCreature, SeventhCreature
from Inferno import FirstCreature, SecondCreature, ThirdCreature, \
    FourthCreature, FifthCreature, SixthCreature, SeventhCreature
from Mage import FirstCreature, SecondCreature, ThirdCreature, \
    FourthCreature, FifthCreature, SixthCreature, SeventhCreature

window = None
fullscreen = False


def draw_button(colour: tuple, coordinates: tuple, name: str, font: int = 40):
    """
    :param font: Font of text
    :param colour: background colour
    :param coordinates: where should button be placed
    :param name: Button name
    :return: None
    Prints button in correct place
    """
    global window
    pygame.draw.rect(window, colour,
                     (coordinates[0],
                      coordinates[1],
                      coordinates[2],
                      coordinates[3]))
    fond = pygame.font.Font(None, 35)
    text = fond.render(name, True, [218, 165, 32])
    window.blit(text, [coordinates[0] + coordinates[2] // 100 + 1, coordinates[
        1] + coordinates[3] // 100 + 1])


def draw_some_buttons(count: int, names: list, paper_size: tuple):
    """
    :param count: Count of buttons that should be drawn
    :param names: list of names of buttons
    :param paper_size: size of menu
    :return: coordinats of all buttons
    """
    answer = []
    for number in range(count):
        draw_button((128, 0, 0),
                    (paper_size[0] + 20,
                     paper_size[1] + 20 + 10 * number + number *
                     (paper_size[3] - 40 - 10 * (count - 1)) // count,
                     paper_size[2] - 40,
                     (paper_size[3] - 40 - 10 * (count - 1)) // count),
                    names[number])
        answer += [(paper_size[0] + 20,
                    paper_size[1] + 20 + 10 * number + number *
                    (paper_size[3] - 40 - 10 * (count - 1)) // count,
                    paper_size[2] - 40,
                    (paper_size[3] - 40 - 10 * (count - 1)) // count)]
    return answer


def create_window_of_the_same_size():
    """
    :return: nothing
    This function is used to create window of already chosen size
    """
    size = [pygame.display.get_surface().get_width(),
            pygame.display.get_surface().get_height()]
    global window
    global fullscreen
    if fullscreen:
        window = pygame.display.set_mode((size[0], size[1]), pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((size[0], size[1]))
    if os.name == "nt":
        background_image = pygame.image.load(str(os.path.abspath(
            __file__)).split("Game")[0] + str(size[0]) + "x" + str(size[1])
                                             + ".jpg")
    else:
        background_image = pygame.image.load(
            str(size[0]) + "x" + str(size[1]) +
            ".jpg")
    window.blit(background_image, [0, 0])
    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")


def create_window(length: int = 800, width: int = 600, update = True):
    """
    :param length: Length of screen
    :param width: Width of screen
    :return: array of buttons
    Creating window of game(depends on format)
    Make main buttons
    """
    if os.name == "nt":
        user32 = ctypes.windll.user32
        current_w = user32.GetSystemMetrics(0)
        current_h = user32.GetSystemMetrics(1)
        background_image = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + str(length) + "x" + str(width) + ".jpg")
    else:
        info_object = str(get_monitors()).split("=")
        current_w = int(info_object[3].split(",")[0])
        current_h = int(info_object[4].split(",")[0])
        background_image = pygame.image.load(str(length) + "x" + str(width) +
                                             ".jpg")
    if current_w < length or current_h < width:
        print("you can't choose that. Default was set")
        length = 800
        width = 600
        if os.name == "nt":
            background_image = pygame.image.load(
                str(os.path.abspath(__file__)).split(
                    "Game")[0] + str(length) + "x" + str(width) + ".jpg")
        else:
            background_image = pygame.image.load(
                str(length) + "x" + str(width) +
                ".jpg")
    global window
    global fullscreen
    if fullscreen:
        window = pygame.display.set_mode((length, width),
                                         pygame.HWSURFACE | pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((length, width))
    window.blit(background_image, [0, 0])
    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 3, width // 3, length // 3, width // 3))
    buttons = draw_some_buttons(4, ["Start playing", "Options", "Information",
                                    "Exit"],
                                (length // 3, width // 3, length // 3,
                                 width // 3))
    if update:
        pygame.display.update()
    return buttons


def start_menu():
    """
    :return: array of buttons on start menu
    Creating start menu
    """
    size = [pygame.display.get_surface().get_width(),
            pygame.display.get_surface().get_height()]
    create_window_of_the_same_size()
    fond = pygame.font.Font(None, 40)
    text = fond.render("Coming soon", True, [0, 0, 0])
    window.blit(text, [size[0] // 3 + 24, size[1] // 3])
    draw_button((128, 0, 0),
                (size[0] // 3 + 24,
                 size[1] // 3 + 50 + 3 * (
                         size[1] // 3 - 70) // 4,
                 size[0] // 3 - 50,
                 (size[1] // 3 - 70) // 4),
                "Return to main")
    pygame.display.update()
    return [(size[0] // 3 + 24,
             size[1] // 3 + 50 + 3 * (size[1] // 3 - 70) // 4,
             size[0] // 3 - 50,
             (size[1] // 3 - 70) // 4)]


def option_menu():
    """
    :return: array of option's buttons
    """
    size_of_options = [pygame.display.get_surface().get_width(),
                       pygame.display.get_surface().get_height()]
    create_window_of_the_same_size()
    length = size_of_options[0]
    width = size_of_options[1]
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 3,
                      width // 5,
                      length // 3,
                      2 * width // 5 + (2 * width // 5 - 90) // 6 + 20))
    if os.name == "nt":
        user32 = ctypes.windll.user32
        current_w = user32.GetSystemMetrics(0)
        current_h = user32.GetSystemMetrics(1)
    else:
        info_object = str(get_monitors()).split("=")
        current_w = int(info_object[3].split(",")[0])
        current_h = int(info_object[4].split(",")[0])
    button_names = []
    button_name = "800x600"
    if current_w < 800 or current_h < 600:
        button_name += "*"
    button_names += [button_name]
    button_name = "1178x663"
    if current_w < 1178 or current_h < 663:
        button_name += "*"
    button_names += [button_name]
    button_name = "1280x720"
    if current_w < 1280 or current_h < 720:
        button_name += "*"
    button_names += [button_name]
    button_name = "1920x1080"
    if current_w < 1920 or current_h < 1080:
        button_name += "*"
    button_names += [button_name]
    button_name = "1600x800"
    if current_w < 1600 or current_h < 800:
        button_name += "*"
    button_names += [button_name]
    button_names += ["Fullscreen", "Return"]
    buttons = draw_some_buttons(len(button_names), button_names,
                                (length // 3,
                                 width // 5,
                                 length // 3,
                                 2 * width // 5 + (
                                         2 * width // 5 - 90) // 6 + 20))
    fond = pygame.font.Font(None, 40)
    text = fond.render("* means you can't choose this parametr", True,
                       [255, 255, 255])
    window.blit(text, [length // 4, width - 40])

    pygame.display.update()
    return buttons


def information_menu():
    """
    :return: information buttons
    Create information window
    """
    create_window_of_the_same_size()
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 3,
                      width // 3,
                      length // 3,
                      width // 3))
    buttons = draw_some_buttons(4, ["Heroes", "Spells", "Units", "Return"],
                                (length // 3,
                                 width // 3,
                                 length // 3,
                                 width // 3))
    pygame.display.update()
    return buttons


def spell_menu():
    """
    :return: spell menu buttons
    Create a spell menu
    """
    create_window_of_the_same_size()
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 3,
                      width // 3,
                      length // 3,
                      width // 3))
    buttons = draw_some_buttons(5, ["Dark", "Destructive", "Light",
                                    "Summoning", "Return"],
                                (length // 3,
                                 width // 3,
                                 length // 3,
                                 width // 3))
    pygame.display.update()
    return buttons


def choose_class_display():
    """
    :return: buttons of choosing class
    Create a window to choose class
    """
    create_window_of_the_same_size()
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (3 * length // 8,
                      width // 5,
                      3 * length // 8,
                      3 * width // 5))
    buttons = draw_some_buttons(7, ["Orden",
                                    "Necropolis",
                                    "Inferno",
                                    "NatureProtection",
                                    "ShadowLeague",
                                    "Mage",
                                    "Return"],
                                (3 * length // 8,
                                 width // 5,
                                 3 * length // 8,
                                 3 * width // 5))
    pygame.display.update()
    return buttons


def show_heroes(class_name: str):
    """
    :param class_name: Witch class should be shown
    :return: buttons coordinates
    Create Hero menu
    """
    create_window_of_the_same_size()
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
    buttons = draw_some_buttons(2, hero_list,
                                (length // 3,
                                 width // 3,
                                 length // 3,
                                 2 * width // 9))
    buttons += draw_some_buttons(1, ["Return"],
                                 (length // 3,
                                  width // 3 - 30 + 2 * width // 9,
                                  length // 3,
                                  width // 9 + 15))
    pygame.display.update()
    return buttons


def show_units(class_name: str):
    """
    :param class_name: what class should be shown
    :return: buttons for units
    Create menu for information of Creatures
    """
    create_window_of_the_same_size()
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    unit_list = []
    if class_name == "Orden":
        unit_list = ["Villager",
                     "Archer",
                     "Footman",
                     "Griffin",
                     "Priest",
                     "Cavalier",
                     "Angel",
                     "Conscript",
                     "Marksman",
                     "Squire",
                     "Imperial Griffin",
                     "Inquisitor",
                     "Paladin",
                     "Archangel"]
    elif class_name == "Necropolis":
        unit_list = ["Skeleton",
                     "Zombie",
                     "Ghost",
                     "Vampire",
                     "Lich",
                     "Wight",
                     "Bone Dragon",
                     "Skeleton Archer",
                     "Plague Zombie",
                     "Spectre",
                     "Vampire Lord",
                     "Archlich",
                     "Wraith",
                     "Spectral Dragon"]
    elif class_name == "Mage":
        unit_list = ["Gremlin",
                     "Stone Gargoyle",
                     "Iron Golem",
                     "Mage",
                     "Djinn",
                     "Rakshasa Rani",
                     "Colossus",
                     "Master Gremlin",
                     "Obsidian Gargoyle",
                     "Steel Golem",
                     "Archmage",
                     "Djinn Sultan",
                     "Rakshasa Raja",
                     "Titan"]
    elif class_name == "ShadowLeague":
        unit_list = ["Scout",
                     "Blood Maiden",
                     "Minotaur",
                     "Dark Rider",
                     "Hydra",
                     "Shadow Witch",
                     "Shadow Dragon",
                     "Assassin",
                     "Blood Fury",
                     "Minotaur Guard",
                     "Grim Rider",
                     "Deep Hydra",
                     "Shadow Matriarch",
                     "Black Dragon"]
    elif class_name == "NatureProtection":
        unit_list = ["Pixie",
                     "Blade Dancer",
                     "Hunter",
                     "Druid",
                     "Unicorn",
                     "Treant",
                     "Green Dragon",
                     "Sprite",
                     "War Dancer",
                     "Master Hunter",
                     "Druid Elder",
                     "Silver Unicorn",
                     "Ancien Treant",
                     "Emerald Dragon"]
    elif class_name == "Inferno":
        unit_list = ["Imp",
                     "Horned Demon",
                     "Hell Hound",
                     "Succubus",
                     "Hell Charger",
                     "Pit Fiend",
                     "Devil",
                     "Familiar",
                     "Horned Overseer",
                     "Cerberus",
                     "Succubus Mistress",
                     "Nightmare",
                     "Pit Lord",
                     "Arch Devil"]
    else:
        print("Something went wrong. Please, tell Anastasia Kemova about that "
              "kemovakemova.aiu@phystech.edu (wrong classname)")
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 8,
                      width // 5,
                      3 * length // 4,
                      3 * width // 5 + 3 * width // 35))
    buttons = draw_some_buttons(7, unit_list[:7],
                                (length // 8,
                                 width // 5,
                                 3 * length // 8,
                                 3 * width // 5))
    buttons += draw_some_buttons(7, unit_list[7:],
                                 (length // 2,
                                  width // 5,
                                  3 * length // 8,
                                  3 * width // 5))
    buttons += draw_some_buttons(1, ["Return"],
                                 (length // 3,
                                  4 * width // 5 - 30,
                                  length // 3,
                                  width // 7))
    pygame.display.update()
    return buttons, unit_list


def show_unit(unit_name: str):
    """
    :param unit_name: what unit should be shown
    :return: return button
    
    shows information about units
    """
    global opened_catalog
    global array_of_Orden, array_of_Necro, array_of_Mage, array_of_Forest, \
        array_of_Inferno, array_of_Shadows
    global catalogs
    global arrays_list
    global creatures_types
    creature = creatures_types[arrays_list[catalogs.index(
        opened_catalog)].index(unit_name)]
    create_window_of_the_same_size()
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    if os.name == "nt":
        background_image_of_unit = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + "textures/заготовка.png")
    else:
        background_image_of_unit = pygame.image.load("textures/заготовка.png")
    window.blit(background_image_of_unit, [0, 0])
    draw_button((128, 0, 0), (length - 200, width - width // 10, 170, 100),
                "Return")
    if os.name == "nt":
        background_image_of_unit_face = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + unit_name + ".png")
    else:
        background_image_of_unit_face = pygame.image.load("textures/" +
                                                          unit_name + ".png")
    window.blit(background_image_of_unit_face, [40, 60])
    font = pygame.font.Font(None, 20)
    text_to_print = (str(creature.__doc__).split("\n"))
    for number in range(len(text_to_print)):
        text = font.render(text_to_print[number], True,
                           [0, 0, 0])
        window.blit(text, [40, 290 + number * 20])
    pygame.display.update()
    return [(length - 200, width - width // 10, 170, 100)]


def show_hero(hero_name: str):
    """
    :param unit_name: what unit should be shown
    :return:
    """
    create_window_of_the_same_size()
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    if os.name == "nt":
        background_image_of_unit = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + "заготовка.png")
    else:
        background_image_of_unit = pygame.image.load("заготовка.png")
    window.blit(background_image_of_unit, [0, 0])
    draw_button((128, 0, 0), (length - 200, width - width // 10, 170, 100),
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


def button_was_clicked(buttons: list,
                       move_to_page: list,
                       mouse_position: list):
    """
    :param mouse_position: x and t coordinates in click
    :param buttons: what buttons are on screen now
    :param move_to_page: what pages will be next
    :return: was it clicked or not, index of button and next page name
    """
    for button in buttons:
        if button[0] < mouse_position[0] < button[0] + button[2] and \
                button[1] < mouse_position[1] < button[1] + button[3]:
            return [True,
                    move_to_page[buttons.index(button)]]
    return [False, None]


pygame.init()

creatures_name = []
buttons_list = create_window()
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
                        buttons_list = start_menu()
                    elif page == "Options":
                        buttons_list = option_menu()
                    elif page == "Information":
                        buttons_list = information_menu()
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
                        buttons_list = create_window(size[0], size[1])
                    elif next_page == "Fullscreen":
                        fullscreen = not fullscreen
                        buttons_list = option_menu()
                    else:
                        create_window(int(next_page.split("x")[0]),
                                      int(next_page.split("x")[1]),
                                      False)
                        buttons_list = option_menu()
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
                        buttons_list = create_window(size[0], size[1])
                    elif page == "Spells":
                        buttons_list = spell_menu()
                    elif page == "Heroes" or page == "Units":
                        buttons_list = choose_class_display()
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
                    buttons_list = create_window(size[0], size[1])
        elif page == "Units":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                was_clicked, next_page = button_was_clicked(
                    buttons_list,
                    classes_list + ["Main menu"],
                    [mouse_x, mouse_y]
                )
                if was_clicked:
                    page = next_page + " Units"
                    i = 0
                    if next_page in classes_list:
                        opened_catalog = catalogs[classes_list.index(
                            next_page)]
                        buttons_list, creatures_name = show_units(next_page)
                    elif next_page == "Main menu":
                        page = "Main menu"
                        size = [pygame.display.get_surface().get_width(),
                            pygame.display.get_surface().get_height()]
                        buttons_list = create_window(size[0], size[1])
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
                    buttons_list = information_menu()
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
                        buttons_list = start_menu()
                    elif next_page == "Destructive":
                        buttons_list = start_menu()
                    elif next_page == "Light":
                        buttons_list = start_menu()
                    elif next_page == "Summoning":
                        buttons_list = start_menu()
                    elif next_page == "Information":
                        buttons_list = information_menu()
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
                        buttons_list = show_unit(next_page)
                    elif next_page == "Units":
                        buttons_list = choose_class_display()
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
                    buttons_list = choose_class_display()
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
                    buttons_list = choose_class_display()
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
                    buttons_list = choose_class_display()
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
                    buttons_list = choose_class_display()
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
                    buttons_list = choose_class_display()
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
                    buttons_list = choose_class_display()
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
                    buttons_list, creatures_name = show_units("Inferno")
        elif page in array_of_Forest:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "NatureProtection Units"
                    buttons_list, creatures_name = show_units("Nature "
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
                    buttons_list, creatures_name = show_units("Mage")
        elif page in array_of_Necro:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Necropolis Units"
                    buttons_list, creatures_name = show_units("Necropolis")
        elif page in array_of_Shadows:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "ShadowLeague Units"
                    buttons_list, creatures_name = show_units("ShadowLeague")
        elif page in array_of_Orden:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Orden Units"
                    buttons_list, creatures_name = show_units("Orden")
        elif page == " 	Agrail":
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
