import pygame


def draw_green_cell(window, i, j, width, height):
    size_of_cell = (height * 5 // 6) // 10
    size = (width - size_of_cell * 12) // 2
    pygame.draw.rect(window, (107, 142, 35),
                     (size + j * size_of_cell, 2 + i * size_of_cell, size_of_cell - 1, size_of_cell - 1))
    pygame.display.update()
