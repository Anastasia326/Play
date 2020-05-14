import ctypes

import pygame
import os

from screeninfo import get_monitors

from Working_with_textures.draw_some_buttons import draw_some_buttons


def cycle(x, y, length, width, window, size_of_cell_1, size_of_cell_2, map_,
          number1=10, number_2=10, number_3=5, number_4=5, ):
    for i in range(x - number1, x + number_2 + 1):
        for j in range(y - number_3, y + number_4 + 1):
            try:
                if os.name == "nt":
                    background_image = pygame.image.load(
                        str(os.path.abspath(__file__)).split(
                            "Working_with_textures")[0] + "Modes\\Textures\\" +
                        map_[i][j].split("Count")[0] + str(length) + "x" + str(
                            width) + ".png")
                else:
                    background_image = pygame.image.load(
                        str(os.path.abspath(__file__)).split(
                            "Working_with_textures")[0] + "Modes/Textures/" +
                        map_[i][j].split("Count")[0] + str(length) + "x" + str(
                            width) + ".png")
                window.blit(background_image,
                            [(i - x + number1) * size_of_cell_1,
                             (j - y + number_3) * size_of_cell_2])
            except:
                pass


def drow_map(window, fullscreen, Name, x, y, map_,
             length: int = 800,
             width: int = 600, k = 1,
             update=True):
    if os.name == "nt":
        user32 = ctypes.windll.user32
        current_w = user32.GetSystemMetrics(0)
        current_h = user32.GetSystemMetrics(1)
        background_image = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Working_with_textures")[0] + "Modes\\Textures\\" + Name + str(
                length) + "x" + str(width) + ".png")
    else:
        info_object = str(get_monitors()).split("=")
        current_w = int(info_object[3].split(",")[0])
        current_h = int(info_object[4].split(",")[0])
        background_image = pygame.image.load(
            str(os.path.abspath(__file__)).split(
                "Working_with_textures")[0] + "Modes/Textures/" + Name + str(
                length) +
            "x" + str(width) +
            ".png")
    if current_w < length or current_h < width:
        print("you can't choose that. Default was set")
        if os.name == "nt":
            background_image = pygame.image.load(
                str(os.path.abspath(__file__)).split(
                    "Working_with_textures")[
                    0] + "Modes\\Textures\\" + Name + str(length) + "x" + str(
                    width) + ".png")
        else:
            background_image = pygame.image.load(
                str(os.path.abspath(__file__)).split(
                    "Working_with_textures")[0] + "Modes/Textures/" +
                Name + str(length) + "x" + str(width) +
                ".png")
    if fullscreen:
        window = pygame.display.set_mode((length, width),
                                         pygame.HWSURFACE | pygame.FULLSCREEN)
    else:
        window = pygame.display.set_mode((length, width))
    window.blit(background_image, [0, 0])
    size_of_cell_1 = length // 21
    size = width - width // 4
    size_of_cell_2 = size // 11
    if x < 10:
        first_coord = 10
    elif len(map_) - 12 > x >= 10:
        first_coord = x
    else:
        first_coord = len(map_) - 11
    if y < 10:
        second_coord = 5
    else:
        second_coord = len(map_[0]) - 6
    cycle(first_coord, second_coord, length, width, window, size_of_cell_1, size_of_cell_2, map_)
    pygame.display.set_caption("Герои меча и магии(Arthur's and Anastasia's "
                               "remake)")
    buttons = draw_some_buttons(window, 2, ["Next turn",
                                            "Exit"],
                                (0, width * 3 // 4  + 10,
                                 length // 4,
                                 width // 4 ), 70, 130, 180, 222, 184, 135, int(25 * k))
    if update:
        pygame.display.update()
    return buttons
