import ctypes

import pygame
import os

from screeninfo import get_monitors


def drow_quick_map(window, fullscreen,  Name, size, size_of_cell, Name_of_map , length: int = 800,
                           width: int = 600,
                           update=True):
    if os.name == "nt":
        user32 = ctypes.windll.user32
        current_w = user32.GetSystemMetrics(0)
        current_h = user32.GetSystemMetrics(1)
        background_image = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + "Modes/" + Name + str(length) + "x" + str(width) \
            + ".jpg")
    else:
        info_object = str(get_monitors()).split("=")
        current_w = int(info_object[3].split(",")[0])
        current_h = int(info_object[4].split(",")[0])
        background_image = pygame.image.load("Modes/" + Name + str(length) +
                                             "x" + str(width) +
                                             ".jpg")
    if current_w < length or current_h < width:
        print("you can't choose that. Default was set")
        length = 800
        width = 600
        if os.name == "nt":
            background_image = pygame.image.load(
                str(os.path.abspath(__file__)).split(
                    "Game")[0] + "Modes/" + Name + str(length) + "x" + str(
                    width) + ".jpg")
        else:
            background_image = pygame.image.load(
                "Modes/" +
                Name + str(length) + "x" + str(width) +
                ".jpg")
    if fullscreen:
        window = pygame.display.set_mode((length, width),
                                         pygame.HWSURFACE | pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((length, width))
    window.blit(background_image, [0, 0])
    if Name_of_map == "Quick":
        size_of_cell = width/21 - 3
    for i in range(size[0]):
        pygame.draw.line(window, (143, 188, 143), (1, 1 + size_of_cell * i), (700, 1 + size_of_cell * i))
    for i in range(size[1]):
        pygame.draw.line(window, (143, 188, 143), (100 + size_of_cell * i, 1), (100 + size_of_cell * i, 501))

    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
    if update:
        pygame.display.update()
    return window
