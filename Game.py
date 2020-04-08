import pygame

window = None


def create_window(length: int = 800, width: int = 600, fullscreen=False):
    info_object = pygame.display.Info()
    if info_object.current_w < length or info_object.current_h < width:
        print("you can't choose that. Default was set")
        length = 800
        width = 600
    global window
    background_image = pygame.image.load(
        str(length) + "x" + str(width) + ".jpg")
    if fullscreen:
        window = pygame.display.set_mode((length, width), pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((length, width))
    window.blit(background_image, [0, 0])
    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")

    background_menu = pygame.draw.rect(window, (205, 133, 63),
                                       (length // 3, width // 3, length // 3,
                                        width // 3))
    start_button = pygame.draw.rect(window, (128, 0, 0),
                                    (length // 3 + 20,
                                     width // 3 + 20,
                                     length // 3 - 40,
                                     (width // 3 - 70) // 4))
    settings_button = pygame.draw.rect(window, (128, 0, 0),
                                       (length // 3 + 20,
                                        width // 3 + 30 + (
                                                width // 3 - 70) // 4,
                                        length // 3 - 40,
                                        (width // 3 - 70) // 4))
    info_button = pygame.draw.rect(window, (128, 0, 0),
                                   (length // 3 + 20,
                                    width // 3 + 40 + 2 * (
                                            width // 3 - 70) // 4,
                                    length // 3 - 40,
                                    (width // 3 - 70) // 4))
    quit_button = pygame.draw.rect(window, (128, 0, 0),
                                   (length // 3 + 20,
                                    width // 3 + 50 + 3 * (
                                            width // 3 - 70) // 4,
                                    length // 3 - 40,
                                    (width // 3 - 70) // 4))
    pygame.display.update()
    return [(length // 3 + 20, width // 3 + 20,
             length // 3 - 40, (width // 3 - 70) // 4),
            (length // 3 + 20, width // 3 + 30 + (width // 3 - 70) // 4,
             length // 3 - 40, (width // 3 - 70) // 4),
            (length // 3 + 20, width // 3 + 40 + 2 * (width // 3 - 70) // 4,
             length // 3 - 40, (width // 3 - 70) // 4),
            (length // 3 + 20, width // 3 + 50 + 3 * (width // 3 - 70) // 4,
             length // 3 - 40, (width // 3 - 70) // 4)]


def start_menu():
    return [(0, 1), 2]


def option_menu():
    return [(0, 1), 2]


pygame.init()
buttons_list = create_window(1178, 663, True)
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        press = pygame.mouse.get_pressed()
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
                buttons_list = start_menu()
            elif buttons_list[1][0] < mouse_x < buttons_list[1][0] + \
                    buttons_list[1][2] and buttons_list[1][1] < mouse_y \
                    < buttons_list[1][1] + buttons_list[1][3]:
                buttons_list = option_menu()
            elif buttons_list[2][0] < mouse_x < buttons_list[2][0] + \
                    buttons_list[2][2] and buttons_list[2][1] < mouse_y \
                    < buttons_list[2][1] + buttons_list[2][3]:
                buttons_list = option_menu()
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
