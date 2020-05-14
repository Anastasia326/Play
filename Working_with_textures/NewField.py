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
                "Working_with_textures")[0] + "Battle/" + Name + str(length) + "x" + str(width) \
            + ".jpg")
    else:
        info_object = str(get_monitors()).split("=")
        current_w = int(info_object[3].split(",")[0])
        current_h = int(info_object[4].split(",")[0])
        background_image = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Working_with_textures")[0] + "Battle/" + Name + str(length) +
                                             "x" + str(width) +
                                             ".jpg")
    if current_w < length or current_h < width:
        print("you can't choose that. Default was set")
        length = 800
        width = 600
        if os.name == "nt":
            background_image = pygame.image.load(
                str(os.path.abspath(__file__)).split(
                    "Working_with_textures")[0] + "Battle/" + Name + str(length) + "x" + str(
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
    for i in range(11):
        pygame.draw.line(window, (143, 188, 143), (100, 1 + size_of_cell * i), (700, 1 + size_of_cell * i))
    for i in range(13):
        pygame.draw.line(window, (143, 188, 143), (100 + size_of_cell * i, 1), (100 + size_of_cell * i, 501))

    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
    if update:
        pygame.display.update()
    return window
