import ctypes
from Working_with_textures.NewField import create_window_of_Field
from Working_with_textures.arrays import classes_list
from Working_with_textures.draw_some_buttons import draw_some_buttons
from Working_with_textures.draw_button import draw_button
import pygame
import os

from screeninfo import get_monitors

from Working_with_textures.draw_some_buttons import draw_some_buttons


def create_window_choise(window, fullscreen, k, length: int = 800,
                         height: int = 600,
                         update=True):
    size_of_cell = (height * 5 // 6) // 10
    size = (length - size_of_cell * 12) // 2
    window = create_window_of_Field(window, fullscreen, "Field", length, height)
    draw_button(window, (255, 215, 0),
                (size, height * 5 // 6 + 10, size_of_cell * 12, height // 6 - 20))
    pygame.display.update()
    buttons = []
    size_button = size_of_cell * 12
    for i in range(len(classes_list)//2):
        buttons += draw_some_buttons(window,
                                     2,
                                     classes_list[i*2:(i + 1)*2],
                                     (size + size_button // 3 * i, height * 5 // 6, size_button // 3, 1 * height // 6),
                                     255, 215, 0, 85, 107, 47, int(20 * k))

    pygame.display.update()
    if update:
        pygame.display.update()
    return window, buttons
