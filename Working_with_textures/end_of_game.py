import pygame

from Working_with_textures.create_window_of_the_same_size import create_window_of_the_same_size
from Working_with_textures.draw_some_buttons import draw_some_buttons


def end_of_game(window, fullscreen, length, width, k):
    create_window_of_the_same_size(window, fullscreen)
    pygame.draw.rect(window,
                     (147, 112, 219),
                     (length // 2 - length // 7,
                      width // 2,
                      length * 2 // 7,
                      width // 7))

    font = pygame.font.SysFont('dejavuserif', int(80 * k))
    text = font.render("Game over !", True, (0, 0, 128))
    window.blit(text, (length * 2 // 8, width // 4))
    buttons = draw_some_buttons(window, 1,
                                ["    Exit"],
                                (length // 2 - length // 7,
                                 width // 2,
                                 length * 2 // 7,
                                 width // 7), 147, 112, 219, 0, 0, 128, int(50 * k))
    pygame.display.update()
    return buttons
