import pygame
from screeninfo import get_monitors
import os
import ctypes

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
    fond = pygame.font.Font(None, 40)
    text = fond.render(name, True, [0, 0, 0])
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


def create_window(length: int = 800, width: int = 600):
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
            background_image = pygame.image.load(str(length) + "x" + str(width) +
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
                                    "Nature Protection",
                                    "Shadow League",
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
    elif class_name == "Shadow League":
        hero_list = ["Railag", "Shadia"]
    elif class_name == "Nature Protection":
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
    elif class_name == "Shadow League":
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
    elif class_name == "Nature Protection":
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
    :return:
    """
    pass


pygame.init()

creatures_name = []
buttons_list = create_window()
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
                if buttons_list[3][0] < mouse_x < buttons_list[3][0] + \
                        buttons_list[3][2] and buttons_list[3][1] < mouse_y \
                        < buttons_list[3][1] + buttons_list[3][3]:
                    run = False
                elif buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Start Menu"
                    buttons_list = start_menu()
                elif buttons_list[1][0] < mouse_x < buttons_list[1][0] + \
                        buttons_list[1][2] and buttons_list[1][1] < mouse_y \
                        < buttons_list[1][1] + buttons_list[1][3]:
                    i = 0
                    page = "Options"
                    buttons_list = option_menu()
                elif buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    page = "Information"
                    buttons_list = information_menu()
                    i = 0
        elif page == "Options":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Main menu"
                    buttons_list = create_window(800, 600)
                elif buttons_list[1][0] < mouse_x < buttons_list[1][0] + \
                        buttons_list[1][2] and buttons_list[1][1] < mouse_y \
                        < buttons_list[1][1] + buttons_list[1][3]:
                    i = 0
                    page = "Main menu"
                    buttons_list = create_window(1178, 663)
                elif buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Main menu"
                    buttons_list = create_window(1280, 720)
                elif buttons_list[3][0] < mouse_x < buttons_list[3][0] + \
                        buttons_list[3][2] and buttons_list[3][1] < mouse_y \
                        < buttons_list[3][1] + buttons_list[3][3]:
                    i = 0
                    page = "Main menu"
                    buttons_list = create_window(1920, 1080)
                elif buttons_list[4][0] < mouse_x < buttons_list[4][0] + \
                        buttons_list[4][2] and buttons_list[4][1] < mouse_y \
                        < buttons_list[4][1] + buttons_list[4][3]:
                    i = 0
                    page = "Main menu"
                    buttons_list = create_window(1600, 800)
                elif buttons_list[5][0] < mouse_x < buttons_list[5][0] + \
                        buttons_list[5][2] and buttons_list[5][1] < mouse_y \
                        < buttons_list[5][1] + buttons_list[5][3]:
                    i = 0
                    page = "Main menu"
                    fullscreen = not fullscreen
                    size = [pygame.display.get_surface().get_width(),
                            pygame.display.get_surface().get_height()]
                    buttons_list = create_window(size[0], size[1])
                elif buttons_list[6][0] < mouse_x < buttons_list[6][0] + \
                        buttons_list[6][2] and buttons_list[6][1] < mouse_y \
                        < buttons_list[6][1] + buttons_list[6][3]:
                    i = 0
                    page = "Main menu"
                    size = [pygame.display.get_surface().get_width(),
                            pygame.display.get_surface().get_height()]
                    buttons_list = create_window(size[0], size[1])
        elif page == "Information":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[3][0] < mouse_x < buttons_list[3][0] + \
                        buttons_list[3][2] and buttons_list[3][1] < mouse_y \
                        < buttons_list[3][1] + buttons_list[3][3]:
                    i = 0
                    page = "Main menu"
                    size = [pygame.display.get_surface().get_width(),
                            pygame.display.get_surface().get_height()]
                    buttons_list = create_window(size[0], size[1])
                elif buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Heroes"
                    buttons_list = choose_class_display()
                elif buttons_list[1][0] < mouse_x < buttons_list[1][0] + \
                        buttons_list[1][2] and buttons_list[1][1] < mouse_y \
                        < buttons_list[1][1] + buttons_list[1][3]:
                    i = 0
                    page = "Spells"
                    buttons_list = spell_menu()
                elif buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    page = "Units"
                    buttons_list = choose_class_display()
                    i = 0
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
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Orden Units"
                    buttons_list, creatures_name = show_units("Orden")
                elif buttons_list[1][0] < mouse_x < buttons_list[1][0] + \
                        buttons_list[1][2] and buttons_list[1][1] < mouse_y \
                        < buttons_list[1][1] + buttons_list[1][3]:
                    i = 0
                    page = "Necropolis Units"
                    buttons_list, creatures_name = show_units("Necropolis")
                elif buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Inferno Units"
                    buttons_list, creatures_name = show_units("Inferno")
                elif buttons_list[3][0] < mouse_x < buttons_list[3][0] + \
                        buttons_list[3][2] and buttons_list[3][1] < mouse_y \
                        < buttons_list[3][1] + buttons_list[3][3]:
                    page = "Nature Protection Units"
                    buttons_list, creatures_name = show_units(
                        "Nature Protection")
                    i = 0
                elif buttons_list[4][0] < mouse_x < buttons_list[4][0] + \
                        buttons_list[4][2] and buttons_list[4][1] < mouse_y \
                        < buttons_list[4][1] + buttons_list[4][3]:
                    page = "Shadow League Units"
                    buttons_list, creatures_name = show_units("Shadow League")
                    i = 0
                elif buttons_list[5][0] < mouse_x < buttons_list[5][0] + \
                        buttons_list[5][2] and buttons_list[5][1] < mouse_y \
                        < buttons_list[5][1] + buttons_list[5][3]:
                    page = "Mage Units"
                    buttons_list, creatures_name = show_units("Mage")
                    i = 0
                elif buttons_list[6][0] < mouse_x < buttons_list[6][0] + \
                        buttons_list[6][2] and buttons_list[6][1] < mouse_y \
                        < buttons_list[6][1] + buttons_list[6][3]:
                    page = "Information"
                    buttons_list = information_menu()
                    i = 0
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
                    page = "Nature Protection Heroes"
                    buttons_list = show_heroes("Nature Protection")
                    i = 0
                elif buttons_list[4][0] < mouse_x < buttons_list[4][0] + \
                        buttons_list[4][2] and buttons_list[4][1] < mouse_y \
                        < buttons_list[4][1] + buttons_list[4][3]:
                    page = "Shadow League Heroes"
                    buttons_list = show_heroes("Shadow League")
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
                if buttons_list[0][0] < mouse_x < buttons_list[0][0] + \
                        buttons_list[0][2] and buttons_list[0][1] < mouse_y \
                        < buttons_list[0][1] + buttons_list[0][3]:
                    i = 0
                    page = "Dark"
                    size = [pygame.display.get_surface().get_width(),
                            pygame.display.get_surface().get_height()]
                    buttons_list = create_window(size[0], size[1])
                elif buttons_list[1][0] < mouse_x < buttons_list[1][0] + \
                        buttons_list[1][2] and buttons_list[1][1] < mouse_y \
                        < buttons_list[1][1] + buttons_list[1][3]:
                    i = 0
                    page = "Destructive"
                    buttons_list = choose_class_display()
                elif buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Light"
                    buttons_list = spell_menu()
                elif buttons_list[3][0] < mouse_x < buttons_list[3][0] + \
                        buttons_list[3][2] and buttons_list[3][1] < mouse_y \
                        < buttons_list[3][1] + buttons_list[3][3]:
                    page = "Summoning"
                    buttons_list = choose_class_display()
                    i = 0
                elif buttons_list[4][0] < mouse_x < buttons_list[4][0] + \
                        buttons_list[4][2] and buttons_list[4][1] < mouse_y \
                        < buttons_list[4][1] + buttons_list[4][3]:
                    page = "Information"
                    buttons_list = information_menu()
                    i = 0
        elif page == "Orden Units":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[14][0] < mouse_x < buttons_list[14][0] + \
                        buttons_list[14][2] and buttons_list[14][1] < mouse_y \
                        < buttons_list[14][1] + buttons_list[14][3]:
                    i = 0
                    page = "Units"
                    buttons_list = choose_class_display()
        elif page == "Necropolis Units":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[14][0] < mouse_x < buttons_list[14][0] + \
                        buttons_list[14][2] and buttons_list[14][1] < mouse_y \
                        < buttons_list[14][1] + buttons_list[14][3]:
                    i = 0
                    page = "Units"
                    buttons_list = choose_class_display()
                else:
                    for index in range(14):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[index][
                            3]:
                            i = 0
                            page = creatures_name[i]
                            buttons_list = show_unit(creatures_name[i])
        elif page == "Nature Protection Units":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[14][0] < mouse_x < buttons_list[14][0] + \
                        buttons_list[14][2] and buttons_list[14][1] < mouse_y \
                        < buttons_list[14][1] + buttons_list[14][3]:
                    i = 0
                    page = "Units"
                    buttons_list = choose_class_display()
                else:
                    for index in range(14):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[index][3]:
                            i = 0
                            page = creatures_name[i]
                            buttons_list = show_unit(creatures_name[i])
        elif page == "Shadow League Units":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[14][0] < mouse_x < buttons_list[14][0] + \
                        buttons_list[14][2] and buttons_list[14][1] < mouse_y \
                        < buttons_list[14][1] + buttons_list[14][3]:
                    i = 0
                    page = "Units"
                    buttons_list = choose_class_display()
                else:
                    for index in range(14):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[index][3]:
                            i = 0
                            page = creatures_name[i]
                            buttons_list = show_unit(creatures_name[i])
        elif page == "Inferno Units":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[14][0] < mouse_x < buttons_list[14][0] + \
                        buttons_list[14][2] and buttons_list[14][1] < mouse_y \
                        < buttons_list[14][1] + buttons_list[14][3]:
                    i = 0
                    page = "Units"
                    buttons_list = choose_class_display()
                else:
                    for index in range(15):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[
                            index][3]:
                            i = 0
                            page = creatures_name[i]
                            buttons_list = show_unit(creatures_name[i])
        elif page == "Mage Units":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[14][0] < mouse_x < buttons_list[14][0] + \
                        buttons_list[14][2] and buttons_list[14][1] < mouse_y \
                        < buttons_list[14][1] + buttons_list[14][3]:
                    i = 0
                    page = "Units"
                    buttons_list = choose_class_display()
                else:
                    for index in range(14):
                        if buttons_list[index][0] < mouse_x < buttons_list[
                            index][0] + buttons_list[index][2] and \
                                buttons_list[index][1] < mouse_y < \
                                buttons_list[index][1] + buttons_list[index][
                            3]:
                            i = 0
                            page = creatures_name[i]
                            buttons_list = show_unit(creatures_name[i])
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
        elif page == "Nature Protection Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Heroes"
                    buttons_list = choose_class_display()
        elif page == "Shadow League Heroes":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = pos[0], pos[1]
                if buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                        buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                        < buttons_list[2][1] + buttons_list[2][3]:
                    i = 0
                    page = "Heroes"
                    buttons_list = choose_class_display()
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
            print("Something went wrong. "
                  "Please, tell Anastasia Kemova about that kemova"
                  "kemova.aiu@phystech.edu")
            run = False

pygame.quit()
