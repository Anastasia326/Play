import pygame

def map_draw(window, karta):
    for i in range(10):
        for j in range(12):
            if karta[i][j] is not None:
                background_image_of_unit_face = pygame.image.load("../textures/" +
                                                                  karta[i][j] + ".png")
                window.blit(background_image_of_unit_face, [100 + j * 50, 2 + i * 50])
                pygame.display.update()
