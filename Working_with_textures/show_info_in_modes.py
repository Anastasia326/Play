import os

import pygame

from Working_with_textures.draw_button import draw_button


def show_resources(window, resources: dict, length: int = 800,
                   width: int = 600, k=1):
    array = list(resources.items())
    for i in array:
        try:
            if os.name == "nt":
                background_image = pygame.image.load(
                    str(os.path.abspath(__file__)).split(
                        "Working_with_textures")[0] + "Modes\\Textures\\" +
                    i[0] + str(length) + "x" + str(
                        width) + ".png")
            else:
                background_image = pygame.image.load(
                    str(os.path.abspath(__file__)).split(
                        "Working_with_textures")[0] + "Modes/Textures/" +
                    i[0] + str(length) + "x" + str(
                        width) + ".png")
            window.blit(background_image,
                        [length // 4 + array.index(i) * length // 10,
                         width * 4 // 5])
            draw_button(window,
                        (0, 100, 0),
                        (length // 4 + array.index(i) * length // 10,
                         width * 191 // 220,
                         0,
                         0),
                        str(i[1]),
                        size=(20 * k))
        except:
            pass
    pygame.display.update()


def show_moves(window, moves, length: int = 800,
               width: int = 600, k=1):
    draw_button(window,
                (0, 100, 0),
                (length * 16 // 19,
                 width * 4 // 5,
                 0,
                 0),
                "Moves Left",
                size=(20 * k))
    draw_button(window,
                (0, 100, 0),
                (length * 16 // 19,
                 width * 191 // 220,
                 0,
                 0),
                str(moves),
                size=(20 * k))
    pygame.display.update()
