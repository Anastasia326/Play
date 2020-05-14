import pygame


def write_what_happened(text, window, length = 800, height = 600):
    font = pygame.font.SysFont('dejavuserif', 40)
    text_ = font.render(text, True, (255, 215, 0))
    window.blit(text_, (length // 8, (height // 6) * 5))
    pygame.display.update()
