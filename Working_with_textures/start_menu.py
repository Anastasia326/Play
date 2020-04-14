import pygame

from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size
from Working_with_textures.draw_button import draw_button


def start_menu(window, fullscreen):
    """
    :return: array of buttons on start menu
    Creating start menu
    """
    size = [pygame.display.get_surface().get_width(),
            pygame.display.get_surface().get_height()]
    create_window_of_the_same_size(window, fullscreen)
    fond = pygame.font.Font(None, 40)
    text = fond.render("Coming soon", True, [0, 0, 0])
    window.blit(text, [size[0] // 3 + 24, size[1] // 3])
    draw_button(window, (128, 0, 0),
                (size[0] // 3 + 24,
                 size[1] // 3 + 50 + 3 * (
                         size[1] // 3 - 70) // 4,
                 size[0] // 3 - 50,
                 (size[1] // 3 - 70) // 4),
                "Return to main")
    pygame.display.update()
    return [(size[0] // 3 + 24,
             size[1] // 3 + 50 + 3 * (size[1] // 3 - 70) // 4,
             size[0] // 3 - 50,
             (size[1] // 3 - 70) // 4)]
