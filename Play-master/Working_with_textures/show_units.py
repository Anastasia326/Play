import pygame
from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size
from Working_with_textures.draw_some_buttons import draw_some_buttons


def show_units(window, fullscreen, classes_list, arrays_list, class_name: str):
    """
    :param arrays_list:
    :param classes_list:
    :param fullscreen:
    :param window:
    :param class_name: what class should be shown
    :return: buttons for units
    Create menu for information of Creatures
    """
    create_window_of_the_same_size(window, fullscreen)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    unit_list = arrays_list[classes_list.index(class_name)]
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 8,
                      width // 5,
                      3 * length // 4,
                      3 * width // 5 + 3 * width // 35))
    buttons = draw_some_buttons(window, 7, unit_list[:7],
                                (length // 8,
                                 width // 5,
                                 3 * length // 8,
                                 3 * width // 5))
    buttons += draw_some_buttons(window, 7, unit_list[7:],
                                 (length // 2,
                                  width // 5,
                                  3 * length // 8,
                                  3 * width // 5))
    buttons += draw_some_buttons(window, 1, ["Return"],
                                 (length // 3,
                                  4 * width // 5 - 30,
                                  length // 3,
                                  width // 7))
    pygame.display.update()
    return buttons, unit_list
