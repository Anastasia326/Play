import ctypes
from Working_with_textures.NewField import create_window_of_Field
from Working_with_textures.draw_some_buttons import draw_some_buttons
from Working_with_textures.draw_button import draw_button
import pygame
import os

from screeninfo import get_monitors

from Working_with_textures.draw_some_buttons import draw_some_buttons


def create_window_choise(window, fullscreen, length: int = 800, width: int = 600,
                  update=True):
    window = create_window_of_Field(window, fullscreen, "Field")
    draw_button(window, (255, 215, 0),
                    (100, 510, 600, 80))
    pygame.display.update()
    buttons = draw_some_buttons(window, 2, ["Orden", "Necropolis"], (100,
                         500,
                         200,   # длина надписи
                         1*width // 6), 255, 215, 0, 85, 107, 47, 28) #отступ между ними
    buttons += draw_some_buttons(window, 2, ["Inferno", "Nature Protection"], (300,
                         500,
                         200,   # длина надписи
                         1*width // 6), 255, 215, 0, 85, 107, 47, 28) #отступ между ними
    buttons += draw_some_buttons(window, 2, ["Shadow League", "Mage"], (500,
                         500,
                         200,   # длина надписи
                         1*width // 6), 255, 215, 0, 85, 107, 47, 28) #отступ между ними
    pygame.display.update()
    if update:
        pygame.display.update()
    return window, buttons
