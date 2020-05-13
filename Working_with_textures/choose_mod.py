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
                                 3 * width // 5))
    pygame.display.update()
    return buttons
