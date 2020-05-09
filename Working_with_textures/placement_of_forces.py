import pygame
import os
from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size

def placement_of_forces(window, fullscreen, mouse_x, mouse_y, picture):

    create_window_of_the_same_size(window, fullscreen)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()

    if os.name == "nt":
        background_image_of_unit_face = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Working_with_textures")[0] + picture + ".png")
    else:
        background_image_of_unit_face = pygame.image.load("textures/" +
                                                          picture + ".png")
    window.blit(background_image_of_unit_face, [mouse_x, mouse_y])
    font = pygame.font.Font(None, 20)
    pygame.display.update()
    return [(length - 200, width - width // 10, 170, 100)]
