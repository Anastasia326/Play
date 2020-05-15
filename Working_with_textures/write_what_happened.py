import pygame

def write_what_happened(text, window, length = 800, height = 600, k = 1):
    phrases = text.split("/")
    for i in range(len(phrases)):
        font = pygame.font.SysFont('dejavuserif', int(20 * k))
        text_ = font.render(phrases[i], True, (255, 215, 0))
        size_of_cell = (height * 5 // 6) // 10
        size = (length - size_of_cell * 12) // 2
        window.blit(text_, (size, (height // 6) * 5 + int(20 * k) * i))
    pygame.display.update()

