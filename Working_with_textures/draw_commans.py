import pygame

from Working_with_textures.draw_button2 import draw_button2

pygame.init()

from Working_with_textures.draw_some_buttons import draw_some_buttons
from Working_with_textures.NewField import create_window_of_Field
from Working_with_textures.draw_button import draw_button


def draw_commans(window, fullscreen,  width, height, k):
    window = create_window_of_Field(window, fullscreen, "Field", width, height)
    length = pygame.display.get_surface().get_width()
    width = pygame.display.get_surface().get_height()
    pygame.display.update()
    size_of_cell = (width * 5 // 6) // 10
    size = (length - size_of_cell * 12) // 2
    buttons = draw_some_buttons(window, 7,
                                ["move", "attack", "move_attack", "Wait",
                                 "Defend", "Exit", "range_attack"],
                                (0, 0, size, 7 * size_of_cell), 255, 215, 0, 85, 107, 47, int(k *15))
    buttons += draw_button2(window, fullscreen, (length * 7 // 8 , width * 11 // 12, length // 8, width // 12), "EXIT")
    return buttons
