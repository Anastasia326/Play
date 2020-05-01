import pygame
import os


def create_window_of_the_same_size(window, fullscreen):
    """
    :return: nothing
    This function is used to create window of already chosen size
    """
    size = [pygame.display.get_surface().get_width(),
            pygame.display.get_surface().get_height()]
    if fullscreen:
        window = pygame.display.set_mode((size[0], size[1]), pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((size[0], size[1]))
    if os.name == "nt":
        background_image = pygame.image.load(str(os.path.abspath(
            __file__)).split("Game")[0] + str(size[0]) + "x" + str(size[1])
                                             + ".jpg")
    else:
        background_image = pygame.image.load(
            str(size[0]) + "x" + str(size[1]) +
            ".jpg")
    window.blit(background_image, [0, 0])
    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
