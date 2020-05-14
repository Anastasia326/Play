import pygame


def write_what_happened(text, window, length = 800, height = 600, k = 1):
    font = pygame.font.SysFont('dejavuserif', int(40 * k))
    text_ = font.render(text, True, (255, 215, 0))
    size_of_cell = (height * 5 // 6) // 10
    size = (length - size_of_cell * 12) // 2
    window.blit(text_, (size, (height // 6) * 5))
    pygame.display.update()
