import ctypes
import os

import pygame
from screeninfo import get_monitors

from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size
from Working_with_textures.draw_some_buttons import draw_some_buttons


def option_menu(window, fullscreen):
    """
    :return: array of option's buttons
    """
    size_of_options = [pygame.display.get_surface().get_width(),
                       pygame.display.get_surface().get_height()]
    create_window_of_the_same_size(window, fullscreen)
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
    buttons = draw_some_buttons(window, len(button_names), button_names,
                                (length // 3,
                                 width // 5,
                                 length // 3,
                                 2 * width // 5 + (
                                         2 * width // 5 - 90) // 6 + 20))
    fond = pygame.font.SysFont('dejavuserif', 40)
    text = fond.render("* means you can't choose this parametr", True,
                       [255, 255, 255])
    window.blit(text, [length // 4, width - 40])

    pygame.display.update()
    return buttons
