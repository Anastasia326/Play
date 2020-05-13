import ctypes

import pygame
import os

from screeninfo import get_monitors

from Working_with_textures.draw_some_buttons import draw_some_buttons


def drow_map(window, fullscreen, Name, Name_of_map, x, y, map, length: int = 800,
             width: int = 600,
             update=True):
    if os.name == "nt":
        user32 = ctypes.windll.user32
        current_w = user32.GetSystemMetrics(0)
        current_h = user32.GetSystemMetrics(1)
        background_image = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Game")[0]  + Name + str(length) + "x" + str(width) \
            + ".png")
    else:
        info_object = str(get_monitors()).split("=")
        current_w = int(info_object[3].split(",")[0])
        current_h = int(info_object[4].split(",")[0])
        background_image = pygame.image.load(Name + str(length) +
                                             "x" + str(width) +
                                             ".png")
    if current_w < length or current_h < width:
        print("you can't choose that. Default was set")
        length = 800
        width = 600
        if os.name == "nt":
            background_image = pygame.image.load(
                str(os.path.abspath(__file__)).split(
                    "Game")[0] + Name + str(length) + "x" + str(
                    width) + ".png")
        else:
            background_image = pygame.image.load(
                Name + str(length) + "x" + str(width) +
                ".png")
    if fullscreen:
        window = pygame.display.set_mode((length, width),
                                         pygame.HWSURFACE | pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((length, width))
    window.blit(background_image, [0, 0])
    size_down = 0
    size_of_cell = length // 21
    if Name_of_map == "Quick":
        size_down = 11
    else:
        size_down = 20
    if 39 >= x >= 10 :
       for i in range(x - 10, x + 10):
           for j in range(size_down):
               try:
                   background_image = pygame.image.load(map[i][j].split("Count")[0] + str(length) + "x" + str(width) + ".png")
                   window.blit(background_image, [(i - x + 10) * size_of_cell, j * size_of_cell])
               except:
                   pass
    elif x < 10:
        for i in range(0, 21):
           for j in range(size_down):
               try:
                   background_image = pygame.image.load(map[i][j].split("Count")[0] + str(length) + "x" + str(width) + ".png")
                   window.blit(background_image, [(i) * size_of_cell, j * size_of_cell])
               except:
                   pass
    else:
        for i in range(28, 50):
           for j in range(size_down):
               try:
                   background_image = pygame.image.load(map[i][j].split("Count")[0] + str(length) + "x" + str(width) + ".png")
                   window.blit(background_image, [(i - 28) * size_of_cell, j * size_of_cell])
               except:
                   pass


    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
    buttons = draw_some_buttons(window, 2, ["Exit from the game", "Pass the move to the another player"],
                                (length // 10, width // 6 * 4 + 10, length - 2 * (length // 10),
                                 width // 10 * 3), 255, 127, 80)  # (х, у, длина, ширина)
    if update:
        pygame.display.update()
    return buttons
