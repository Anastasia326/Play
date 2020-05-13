import ctypes
from Working_with_textures.NewField import create_window_of_Field
from Working_with_textures.arrays import classes_list
from Working_with_textures.draw_some_buttons import draw_some_buttons
from Working_with_textures.draw_button import draw_button
import pygame
import os

from screeninfo import get_monitors

from Working_with_textures.draw_some_buttons import draw_some_buttons


def create_window_choise(window, fullscreen, length: int = 800,
                         height: int = 600,
                         update=True):
    window = create_window_of_Field(window, fullscreen, "Field")
    draw_button(window, (255, 215, 0),
                (100, 510, 600, 80))
    pygame.display.update()
    buttons = []
    for i in range(len(classes_list)//2):
        buttons += draw_some_buttons(window,
                                     2,
                                     classes_list[i*2:(i + 1)*2],
                                     (100 + 200 * i, 500, 200, 1 * height // 6),
                                     255, 215, 0, 85, 107, 47, 20)
    pygame.display.update()
    if update:
        pygame.display.update()
    return window, buttons
