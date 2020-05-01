import pygame

from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size
from Working_with_textures.draw_some_buttons import draw_some_buttons


def spell_menu(window, fullscreen):
    """
    :return: spell menu buttons
    Create a spell menu
    """
    create_window_of_the_same_size(window, fullscreen)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 3,
                      width // 3,
                      length // 3,
                      width // 3))
    buttons = draw_some_buttons(window, 5, ["Dark", "Destructive", "Light",
                                            "Summoning", "Return"],
                                (length // 3,
                                 width // 3,
                                 length // 3,
                                 width // 3))
    pygame.display.update()
    return buttons
