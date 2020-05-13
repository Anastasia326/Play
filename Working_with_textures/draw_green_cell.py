import pygame


def draw_green_cell(window, i, j):
    pygame.draw.rect(window, (107, 142, 35),
                     (100 + j * 50, 2 + i * 50, 49, 49))
    pygame.display.update()
