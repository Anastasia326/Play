import ctypes

import pygame
import os

from screeninfo import get_monitors


def create_window_of_Field(window, fullscreen, Name, length: int = 800,
                           width: int = 600,
                           update=True):
    if os.name == "nt":
        user32 = ctypes.windll.user32
        current_w = user32.GetSystemMetrics(0)
        current_h = user32.GetSystemMetrics(1)
        background_image = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + "Battle/" + Name + str(length) + "x" + str(width) \
            + ".jpg")
    else:
        info_object = str(get_monitors()).split("=")
        current_w = int(info_object[3].split(",")[0])
        current_h = int(info_object[4].split(",")[0])
        background_image = pygame.image.load("Battle/" + Name + str(length) +
                                             "x" + str(width) +
                                             ".jpg")
    if current_w < length or current_h < width:
        print("you can't choose that. Default was set")
        length = 800
        width = 600
        if os.name == "nt":
            background_image = pygame.image.load(
                str(os.path.abspath(__file__)).split(
                    "Game")[0] + "Battle/" + Name + str(length) + "x" + str(
                    width) + ".jpg")
        else:
            background_image = pygame.image.load(
                "Battle/" +
                Name + str(length) + "x" + str(width) +
                ".jpg")
    if fullscreen:
        window = pygame.display.set_mode((length, width),
                                         pygame.HWSURFACE | pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((length, width))
    window.blit(background_image, [0, 0])
    size_of_cell = 50
    pygame.draw.line(window, (143, 188, 143), (100, 1), (700, 1))
    pygame.draw.line(window, (143, 188, 143), (100, 1 + size_of_cell),
                     (700, 1 + size_of_cell))
    pygame.draw.line(window, (143, 188, 143), (100, 1 + 2 * size_of_cell),
                     (700, 1 + 2 * size_of_cell))
    pygame.draw.line(window, (143, 188, 143), (100, 1 + 3 * size_of_cell),
                     (700, 1 + 3 * size_of_cell))
    pygame.draw.line(window, (143, 188, 143), (100, 1 + 4 * size_of_cell),
                     (700, 1 + 4 * size_of_cell))
    pygame.draw.line(window, (143, 188, 143), (100, 1 + 5 * size_of_cell),
                     (700, 1 + 5 * size_of_cell))
    pygame.draw.line(window, (143, 188, 143), (100, 1 + 6 * size_of_cell),
                     (700, 1 + 6 * size_of_cell))
    pygame.draw.line(window, (143, 188, 143), (100, 1 + 7 * size_of_cell),
                     (700, 1 + 7 * size_of_cell))
    pygame.draw.line(window, (143, 188, 143), (100, 1 + 8 * size_of_cell),
                     (700, 1 + 8 * size_of_cell))
    pygame.draw.line(window, (143, 188, 143), (100, 1 + 9 * size_of_cell),
                     (700, 1 + 9 * size_of_cell))
    pygame.draw.line(window, (143, 188, 143), (100, 1 + 10 * size_of_cell),
                     (700, 1 + 10 * size_of_cell))
    pygame.draw.line(window, (143, 188, 143), (100, 1), (100, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + size_of_cell, 1),
                     (100 + size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 2 * size_of_cell, 1),
                     (100 + 2 * size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 3 * size_of_cell, 1),
                     (100 + 3 * size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 4 * size_of_cell, 1),
                     (100 + 4 * size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 5 * size_of_cell, 1),
                     (100 + 5 * size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 6 * size_of_cell, 1),
                     (100 + 6 * size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 7 * size_of_cell, 1),
                     (100 + 7 * size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 8 * size_of_cell, 1),
                     (100 + 8 * size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 9 * size_of_cell, 1),
                     (100 + 9 * size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 10 * size_of_cell, 1),
                     (100 + 10 * size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 11 * size_of_cell, 1),
                     (100 + 11 * size_of_cell, 501))
    pygame.draw.line(window, (143, 188, 143), (100 + 12 * size_of_cell, 1),
                     (100 + 12 * size_of_cell, 501))

    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
    if update:
        pygame.display.update()
    return window
