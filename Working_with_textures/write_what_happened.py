import pygame

def write_what_happened(text, window):
    font = pygame.font.SysFont('dejavuserif', 60)
    text_ = font.render(text, True, (255, 215, 0))
    window.blit(text, (120, 730))
