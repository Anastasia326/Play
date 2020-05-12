import pygame

pygame.init()

from Working_with_textures.create_window_of_the_same_size import \
    create_window_of_the_same_size
from Working_with_textures.draw_some_buttons import draw_some_buttons
from Working_with_textures.NewField import create_window_of_Field
from Working_with_textures.draw_button2 import draw_button2
from Working_with_textures.draw_button import draw_button


def chose_with_whom_play(window, fullscreen, name1, name2):
    window = create_window_of_Field(window, fullscreen, "Field")
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    draw_button(window, (255, 215, 0),
                (100, 510, 600, 80), "Choose hero", 85, 107, 47, 60)
    pygame.display.update()
    buttons = draw_button2(window, (255, 215, 0), (2, 2, 90, 30), name1, 85,
                           107, 47, 15)
    buttons += draw_button2(window, (255, 215, 0), (710, 2, 90, 30), name2, 85,
                            107, 47, 15)
    pygame.display.update()
    return buttons
