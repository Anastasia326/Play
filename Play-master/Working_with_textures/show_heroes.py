import pygame

from Working_with_textures.arrays import heroes_list, classes_list
from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size
from Working_with_textures.draw_some_buttons import draw_some_buttons


def show_heroes(window, fullscreen, class_name: str):
    """
    :param class_name: Witch class should be shown
    :return: buttons coordinates
    Create Hero menu
    """
    create_window_of_the_same_size(window, fullscreen)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    hero_list = heroes_list[classes_list.index(class_name)]
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 3,
                      width // 3,
                      length // 3,
                      width // 3))
    buttons = draw_some_buttons(window, 2, hero_list,
                                (length // 3,
                                 width // 3,
                                 length // 3,
                                 2 * width // 9))
    buttons += draw_some_buttons(window, 1, ["Return"],
                                 (length // 3,
                                  width // 3 - 30 + 2 * width // 9,
                                  length // 3,
                                  width // 9 + 15))
    pygame.display.update()
    return buttons, hero_list
