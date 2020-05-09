import os

import pygame

from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size
from Working_with_textures.draw_button import draw_button


def show_hero(window, fullscreen, hero_name: str):
    """
    :param hero_name: what hero should be shown
    :return:
    """
    create_window_of_the_same_size(window, fullscreen)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    if os.name == "nt":
        background_image_of_unit = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + "textures\\заготовка.png")
    else:
        background_image_of_unit = pygame.image.load("textures/заготовка.png")
    window.blit(background_image_of_unit, [0, 0])
    draw_button(window, (128, 0, 0),
                (length - 200, width - width // 10, 170, 100),
                "Return")
    if os.name == "nt":
        background_image_of_unit_face = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0] + "textures\\" + hero_name + ".png")
    else:
        background_image_of_unit_face = pygame.image.load("textures/" +
                                                          hero_name + ".png")
    window.blit(background_image_of_unit_face, [40, 60])
    pygame.display.update()
    return [(length - 200, width - width // 10, 170, 100)]
