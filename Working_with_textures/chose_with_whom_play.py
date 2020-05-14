import pygame

from Working_with_textures.NewField import create_window_of_Field
from Working_with_textures.draw_button2 import draw_button2
from Working_with_textures.draw_button import draw_button


def chose_with_whom_play(window, fullscreen, name1, name2, width, height, k):
    window = create_window_of_Field(window, fullscreen, "Field", width, height)
    size_of_cell = (height * 5 // 6) // 10
    size = (width - size_of_cell * 12) // 2
    draw_button(window, (255, 215, 0),
                (size, height * 5 // 6 + 10, height, width // 10),
                "Choose hero", 85, 107, 47, int(60 * k))
    pygame.display.update()
    buttons = draw_button2(window, (255, 215, 0),
                           (2, 2, size - 10, int(30 * k)), name1, 85,
                           107, 47, int(15 * k))
    buttons += draw_button2(window, (255, 215, 0),
                            (width - size + 10, 2, size - 10, int(30 * k)),
                            name2, 85,
                            107, 47, int(15 * k))
    pygame.display.update()
    return buttons
