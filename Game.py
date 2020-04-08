import pygame
from screeninfo import get_monitors

window = None
fullscreen = False
'''
length, width = 800, 600
print(length, width, (width // 3 - 70) // 4, length // 3 - 50)
length, width = 1178, 663
print(length, width, (width // 3 - 70) // 4, length // 3 - 50)
length, width = 1280, 720
print(length, width, (width // 3 - 70) // 4, length // 3 - 50)
length, width = 1600, 800
print(length, width, (width // 3 - 70) // 4, length // 3 - 50)
length, width = 1920, 1080
print(length, width, (width // 3 - 70) // 4, length // 3 - 50)
'''


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


def create_window(length: int = 800, width: int = 600):
    """
    :param length: Length of screen
    :param width: Width of screen
    :return: array of buttons

    Creating window of game(depends on format)
    Make main buttons
    """
    info_object = str(get_monitors()).split("=")
    current_w = int(info_object[3].split(",")[0])
    current_h = int(info_object[4].split(",")[0])
    if current_w < length or current_h < width:
        print("you can't choose that. Default was set")
        length = 800
        width = 600
    global window
    global fullscreen
    if fullscreen:
        window = pygame.display.set_mode((length, width),
                                         pygame.HWSURFACE | pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((length, width))
    background_image = pygame.image.load(str(length) + "x" + str(width) +
                                         ".jpg")
    window.blit(background_image, [0, 0])
    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 3, width // 3, length // 3, width // 3))
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 3 + 20,
                 length // 3 - 50,
                 (width // 3 - 70) // 4),
                "Start playing")
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 3 + 30 + (
                         width // 3 - 70) // 4,
                 length // 3 - 50,
                 (width // 3 - 70) // 4),
                "Options")
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 3 + 40 + 2 * (
                         width // 3 - 70) // 4,
                 length // 3 - 50,
                 (width // 3 - 70) // 4),
                "Information")
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 3 + 50 + 3 * (
                         width // 3 - 70) // 4,
                 length // 3 - 50,
                 (width // 3 - 70) // 4),
                "Exit")
    pygame.display.update()
    return [(length // 3 + 24, width // 3 + 20,
             length // 3 - 50, (width // 3 - 70) // 4),
            (length // 3 + 24, width // 3 + 30 + (width // 3 - 70) // 4,
             length // 3 - 50, (width // 3 - 70) // 4),
            (length // 3 + 24, width // 3 + 40 + 2 * (width // 3 - 70) // 4,
             length // 3 - 50, (width // 3 - 70) // 4),
            (length // 3 + 24, width // 3 + 50 + 3 * (width // 3 - 70) // 4,
             length // 3 - 50, (width // 3 - 70) // 4)]


def start_menu():
    """
    :return: array of buttons on start menu

    Creating start menu
    """
    size = [pygame.display.get_surface().get_width(),
            pygame.display.get_surface().get_height()]
    global window
    global fullscreen
    if fullscreen:
        window = pygame.display.set_mode((size[0], size[1]), pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((size[0], size[1]))
    background_image = pygame.image.load(str(size[0]) + "x" + str(size[1]) +
                                         ".jpg")
    window.blit(background_image, [0, 0])
    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
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
    global window
    background_image = pygame.image.load(
        str(size_of_options[0]) + "x" + str(size_of_options[1]) +
        ".jpg")
    if fullscreen:
        window = pygame.display.set_mode(
            (size_of_options[0], size_of_options[1]), pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode(
            (size_of_options[0], size_of_options[1]))
    length = size_of_options[0]
    width = size_of_options[1]
    window.blit(background_image, [0, 0])
    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 3,
                      width // 5,
                      length // 3,
                      2 * width // 5 + (2 * width // 5 - 90) // 6 + 20))
    info_object = str(get_monitors()).split("=")
    current_w = int(info_object[3].split(",")[0])
    current_h = int(info_object[4].split(",")[0])
    button_name = "800x600"
    if current_w < 800 or current_h < 600:
        button_name += "*"
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 5 + 20,
                 length // 3 - 50,
                 (2 * width // 5 - 90) // 6),
                button_name,
                25)
    button_name = "1178x663"
    if current_w < 1178 or current_h < 663:
        button_name += "*"
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 5 + 30 + (2 * width // 5 - 90) // 6,
                 length // 3 - 50,
                 (2 * width // 5 - 90) // 6),
                button_name,
                25)
    button_name = "1280x720"
    if current_w < 1280 or current_h < 720:
        button_name += "*"
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 5 + 40 + 2 * (2 * width // 5 - 90) // 6,
                 length // 3 - 50,
                 (2 * width // 5 - 90) // 6),
                button_name,
                25)
    button_name = "1920x1080"
    if current_w < 1920 or current_h < 1080:
        button_name += "*"
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 5 + 50 + (2 * width // 5 - 90) // 2,
                 length // 3 - 50,
                 (2 * width // 5 - 90) // 6),
                button_name,
                25)
    button_name = "1600x800"
    if current_w < 1600 or current_h < 800:
        button_name += "*"
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 5 + 60 + 4 * (2 * width // 5 - 90) // 6,
                 length // 3 - 50,
                 (2 * width // 5 - 90) // 6),
                button_name,
                25)
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 5 + 70 + 5 * (2 * width // 5 - 90) // 6,
                 length // 3 - 50,
                 (2 * width // 5 - 90) // 6),
                "Fullscreen",
                25)
    draw_button((128, 0, 0),
                (length // 3 + 24,
                 width // 5 + 80 + (2 * width // 5 - 90),
                 length // 3 - 50,
                 (2 * width // 5 - 90) // 6),
                "Return",
                25)

    fond = pygame.font.Font(None, 40)
    text = fond.render("* means you can't choose this parametr", True,
                       [255, 255, 255])
    window.blit(text, [length // 4, width - 40])

    pygame.display.update()
    return [(length // 3 + 24,
             width // 5 + 20,
             length // 3 - 50,
             (2 * width // 5 - 90) // 6),
            (length // 3 + 24,
             width // 5 + 30 + (2 * width // 5 - 90) // 6,
             length // 3 - 50,
             (2 * width // 5 - 90) // 6),
            (length // 3 + 24,
             width // 5 + 40 + 2 * (2 * width // 5 - 90)
             // 6, length // 3 - 50,
             (2 * width // 5 - 90) // 6),
            (length // 3 + 24,
             width // 5 + 50 + (2 * width // 5 - 90) // 2,
             length // 3 - 50,
             (2 * width // 5 - 90) // 6),
            (length // 3 + 24,
             width // 5 + 60 + 4 * (2 * width // 5 - 90) // 6,
             length // 3 - 50,
             (2 * width // 5 - 90) // 6),
            (length // 3 + 24,
             width // 5 + 70 + 5 * (2 * width // 5 - 90) // 6,
             length // 3 - 50,
             (2 * width // 5 - 90) // 6),
            (length // 3 + 24,
             width // 5 + 80 + (2 * width // 5 - 90),
             length // 3 - 50,
             (2 * width // 5 - 90) // 6)]


def information_menu():
    return [(0, 1), 2]


pygame.init()

buttons_list = create_window()
print(buttons_list)
run = True

page = "Main menu"
i = 0
while run:
    i += 1
    if i == 10000:
        run = False
    pygame.time.delay(1)
    for event in pygame.event.get():
        '''if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            press = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            print(pos)
            pygame.draw.rect(window, [0, 0, 0],
                             (pos[0], pos[1], 10, 10))
            pygame.display.update()'''
        if page == "Main menu":
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
            if event.type == pygame.QUIT:
                run = False
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
            if event.type == pygame.QUIT:
                run = False
        elif page == "Information":
            if event.type == pygame.QUIT:
                run = False
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
            if event.type == pygame.QUIT:
                run = False
        else:
            print("Something went wrong. "
                  "Please, tell Anastasia Kemova about that kemova"
                  "kemova.aiu@phystech.edu")

pygame.quit()
