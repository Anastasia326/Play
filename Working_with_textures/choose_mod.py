import pygame

from Working_with_textures.arrays import modes
from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size
from Working_with_textures.draw_some_buttons import draw_some_buttons


def choose_mod(window, fullscreen):
    """
    :return: buttons of choosing class
    Create a window to choose class
    """
    create_window_of_the_same_size(window, fullscreen)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    k = 1
    if length == 800:
        k = 1
    elif length == 1178:
        k = 1.25
    elif length == 1280:
        k = 1.45
    elif length == 1920:
        k = 2
    elif length == 1600:
        k = 1.5
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (3 * length // 8,
                      width // 5,
                      3 * length // 8,
                      3 * width // 5))
    buttons = draw_some_buttons(window, 4,
                                modes,
                                (3 * length // 8,
                                 width // 5,
                                 3 * length // 8,
                                 3 * width // 5), 128, 0, 0, 218, 165, 32, int(k *25))
    pygame.display.update()
    return buttons
