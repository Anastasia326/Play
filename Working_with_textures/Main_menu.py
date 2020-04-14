import ctypes

import pygame
import os

from screeninfo import get_monitors

from Working_with_textures.draw_some_buttons import draw_some_buttons


def create_window(window, fullscreen, length: int = 800, width: int = 600,
                  update=True):
    """
    :param window: where to drow
    :param fullscreen: is it fullscreen
    :param update: if it needs to be updated
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
    buttons = draw_some_buttons(window, 4, ["Start playing", "Options",
                                            "Information",
                                            "Exit"],
                                (length // 3, width // 3, length // 3,
                                 width // 3))
    if update:
        pygame.display.update()
    return window, buttons
