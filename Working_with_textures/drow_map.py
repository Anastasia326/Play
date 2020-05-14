import ctypes

import pygame
import os

from screeninfo import get_monitors

from Working_with_textures.draw_some_buttons import draw_some_buttons

def cycle (x, y, number1, number_2, number_3, number_4, length, width, window, size_of_cell, map_):
    for i in range(x - number1, x + number_2):
            for j in range(y - number_3, y + number_4):
                try:
                    background_image = pygame.image.load(
                        str(os.path.abspath(__file__)).split(
                            "Working_with_textures")[0] + "Modes/Textures/" +
                        map_[i][j].split("Count")[0] + str(length) + "x" + str(
                            width) + ".png")
                    window.blit(background_image, [(i - x + number1) * size_of_cell,
                                                   (j - y + number_3) * size_of_cell])
                except:
                    pass


def drow_map(window, fullscreen, Name, Name_of_map, x, y, map_,
             length: int = 800,
             width: int = 600,
             update=True):
    if os.name == "nt":
        user32 = ctypes.windll.user32
        current_w = user32.GetSystemMetrics(0)
        current_h = user32.GetSystemMetrics(1)
        background_image = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + Name + str(length) + "x" + str(width) \
            + ".png")
    else:
        info_object = str(get_monitors()).split("=")
        current_w = int(info_object[3].split(",")[0])
        current_h = int(info_object[4].split(",")[0])
        background_image = pygame.image.load("Textures/" + Name + str(
            length) +
                                             "x" + str(width) +
                                             ".png")
    if current_w < length or current_h < width:
        print("you can't choose that. Default was set")
        length = 800
        width = 600
        if os.name == "nt":
            background_image = pygame.image.load(
                str(os.path.abspath(__file__)).split(
                    "Game")[0] + Name + str(length) + "x" + str(
                    width) + ".png")
        else:
            background_image = pygame.image.load(
                Name + str(length) + "x" + str(width) +
                ".png")
    if fullscreen:
        window = pygame.display.set_mode((length, width),
                                         pygame.HWSURFACE | pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((length, width))
    window.blit(background_image, [0, 0])
    size_of_cell = length // 21

    if len(map_)-22 >= x >= 10:
        if len(map_[0]) - 12 >= y >= 10:
            cycle(x, y, 10, 11, 5, 5, length, width, window, size_of_cell, map_)
        elif y < 10:
            cycle(x, 0, 10, 11, 0, 11, length, width, window, size_of_cell, map_)
        else:
            cycle(x, len(map_[0]) - 7, 10, 11, 5, 5, length, width, window, size_of_cell, map_)
    elif x < 10:
        if len(map_[0]) - 12 >= y >= 10:
            cycle(x, y, 0, 21, 5, 5, length, width, window, size_of_cell, map_)
        elif y < 10:
            cycle(x, 0, 0, 21, 0, 11, length, width, window, size_of_cell, map_)
        else:
            cycle(x, len(map_[0]) - 7, 0, 21, 5, 5, length, width, window, size_of_cell, map_)
    else:
        if len(map_[0]) - 12 >= y >= 10:
            cycle(0, y, len(map_)-22, len(map_)-1, 5, 5, length, width, window, size_of_cell, map_)
        elif y < 10:
            cycle(0, 0, len(map_)-22, len(map_)-1, 0, 11, length, width, window, size_of_cell, map_)
        else:
            cycle(0, len(map_[0]) - 7, len(map_)-22, len(map_)-1, 5, 5, length, width, window, size_of_cell, map_)

    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
    buttons = draw_some_buttons(window, 2, ["Exit from the game",
                                            "Pass the move to the another player"],
                                (length // 10, width // 6 * 4 + 10,
                                 length - 2 * (length // 10),
                                 width // 10 * 3), 255, 127,
                                80)  # (х, у, длина, ширина)
    if update:
        pygame.display.update()
    return buttons
