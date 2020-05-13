import os

import pygame

from Working_with_textures.NewField import create_window_of_Field
from Working_with_textures.write_what_happened import write_what_happened


def map_draw(window, karta, fullscreen, message = "", message2 = ""):
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
                        "Battle\\battle\\" + karta[i][j] + ".png")
                else:
                    background_image_of_unit_face = pygame.image.load(
                        "Battle/battle/" + karta[i][j] + ".png")
                window.blit(background_image_of_unit_face,
                            [100 + j * 50, 2 + i * 50])
                pygame.display.update()
                write_what_happened(message, window)


