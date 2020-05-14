import os

import pygame

from Working_with_textures.NewField import create_window_of_Field
from Working_with_textures.write_what_happened import write_what_happened


def map_draw(window, karta, fullscreen, width, height, k, message=""):
    size_of_cell = (height * 5 // 6) // 10
    size = (width - size_of_cell * 12) // 2
    for i in range(10):
        for j in range(12):
            if karta[i][j] is not None and \
                    (i > 0 and karta[i - 1][j] != karta[i][j] or i == 0) \
                    and \
                    (j > 0 and karta[i][j - 1] != karta[i][j] or j == 0):
                if os.name == "nt":
                    background_image_of_unit_face = pygame.image.load(
                        str(os.path.abspath(__file__)).split(
                            "Working_with_textures")[0] +
                        "Battle\\battle\\" + karta[i][j] + str(width) + "x" + str(height) + ".png")
                else:
                    background_image_of_unit_face = pygame.image.load(
                        str(os.path.abspath(__file__)).split(
                            "Working_with_textures")[0] +
                        "Battle/battle/" + karta[i][j]+ str(width) + "x" + str(height) + ".png")
                window.blit(background_image_of_unit_face,
                            [size + j * size_of_cell, 2 + i * size_of_cell])
                pygame.display.update()
                write_what_happened(message, window, width, height, k)
