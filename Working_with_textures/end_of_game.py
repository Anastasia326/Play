import pygame

from Working_with_textures.create_window_of_the_same_size import create_window_of_the_same_size
from Working_with_textures.draw_some_buttons import draw_some_buttons


def end_of_game(window, fullscreen):
    create_window_of_the_same_size(window, fullscreen)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    pygame.draw.rect(window,
                     (205, 133, 63),
                     (length // 8,
                      width // 2,
                      length * 6 // 8,
                      width // 3))

    font = pygame.font.SysFont('dejavuserif', 60)
    text = font.render("Game over !", True, (255, 215, 0))
    window.blit(text, (length * 2 // 8, width // 3))
    buttons = draw_some_buttons(window, 1,
                                ["Exit"],
                                (length // 8,
                                 width // 2,
                                 length * 6 // 8,
                                 width // 3), 107, 142, 35, 255, 215, 0, 45)
    pygame.display.update()
    return buttons
