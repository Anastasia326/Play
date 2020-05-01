import os

import pygame

from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size
from Working_with_textures.draw_button import draw_button


def show_unit(window, fullscreen, opened_catalog, array_of_Orden,
              array_of_Necro, array_of_Mage, array_of_Forest,
              array_of_Inferno, array_of_Shadows, catalogs,
              arrays_list, creatures_types, unit_name: str):
    """
    :param catalogs:
    :param arrays_list:
    :param creatures_types:
    :param array_of_Forest:
    :param opened_catalog:
    :param array_of_Orden:
    :param array_of_Shadows:
    :param fullscreen:
    :param window:
    :param unit_name: what unit should be shown
    :return: return button

    shows information about units
    """
    types = creatures_types[arrays_list[catalogs.index(
        opened_catalog)].index(unit_name)]
    creature = types

    create_window_of_the_same_size(window, fullscreen)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    if os.name == "nt":
        background_image_of_unit = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + "textures/заготовка.png")
    else:
        background_image_of_unit = pygame.image.load("textures/заготовка.png")
    window.blit(background_image_of_unit, [0, 0])
    draw_button(window, (128, 0, 0),
                (length - 200, width - width // 10, 170, 100),
                "Return")
    if os.name == "nt":
        background_image_of_unit_face = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + unit_name + ".png")
    else:
        background_image_of_unit_face = pygame.image.load("textures/" +
                                                          unit_name + ".png")
    window.blit(background_image_of_unit_face, [40, 60])
    font = pygame.font.Font(None, 20)
    text_to_print = (str(creature.__doc__).split("\n"))
    for number in range(len(text_to_print)):
        text = font.render(text_to_print[number], True,
                           [0, 0, 0])
        window.blit(text, [40, 290 + number * 20])
    pygame.display.update()
    return [(length - 200, width - width // 10, 170, 100)]
