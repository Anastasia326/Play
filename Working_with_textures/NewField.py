import ctypes

import pygame
import os

from screeninfo import get_monitors


def create_window_of_Field(window, fullscreen, Name, length: int = 800,
                           width: int = 600,
                           update=True):
    if os.name == "nt":
        background_image = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Working_with_textures")[0] + "Battle\\" + Name + str(length) +
                "x" + str(width)+ ".jpg")
    else:
        background_image = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Working_with_textures")[0] + "Battle/" + Name + str(length) +
                                             "x" + str(width) +
                                             ".jpg")
    if fullscreen:
        window = pygame.display.set_mode((length, width),
                                         pygame.HWSURFACE | pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((length, width))
    window.blit(background_image, [0, 0])
    size_of_cell = (width * 5 // 6) // 10
    size = (length - size_of_cell * 12) // 2
    for i in range(11):
        pygame.draw.line(window,
                         (143, 188, 143),
                         (size,  size_of_cell * i),
                         (size + size_of_cell * 12, size_of_cell * i))
    for i in range(13):
        pygame.draw.line(window,
                         (143, 188, 143),
                         (size + size_of_cell * i, 0),
                         (size + size_of_cell * i, width * 5 // 6))

    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
    if update:
        pygame.display.update()
    return window
