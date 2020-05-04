import pygame


def map_draw(window, karta):
    for i in range(10):
        for j in range(12):
            if karta[i][j] is not None and \
                    (i > 0 and karta[i - 1][j] is None or i == 0) and \
                    (j > 0 and karta[i][j - 1] is None or j == 0):
                background_image_of_unit_face = pygame.image.load(
                    "Battle/battle/" + karta[i][j] + ".png")
                window.blit(background_image_of_unit_face,
                            [100 + j * 50, 2 + i * 50])
                pygame.display.update()
