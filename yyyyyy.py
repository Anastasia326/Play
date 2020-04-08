import pygame

pygame.init()

background_image = pygame.image.load("gory-zamok-krepost-reka-most.png")

#window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
window = pygame.display.set_mode((600,400))

window.blit(background_image, [0,0])
pygame.display.set_caption("Герои меча и магии -1")

button3 = pygame.draw.rect(window, (205, 133, 63), (170, 140, 280, 180))
button1 = pygame.draw.rect(window, (100, 100, 255), (190, 160, 0, 0))
button2 = pygame.draw.rect(window, (128, 0, 0), (260, 230, 100, 20))
button4 = pygame.draw.rect(window, (128, 0, 0), (260, 260, 100, 20))
button5 = pygame.draw.rect(window, (128, 0, 0), (300, 290, 20, 20))
pygame.display.update()


button = pygame.image.load("nachalo-igry.png")
button.set_colorkey((0, 0, 0))
window.blit(button, button1)
pygame.display.update()

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        press = pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x, mouse_y = pos[0], pos[1]
            if 190 + 240 > mouse_x > 190 and 215 > mouse_y > 160:
                button6 = pygame.draw.rect(window, (205, 133, 63), (170, 140, 280, 180))
                pygame.display.update()
        if event.type == pygame.QUIT:
            run = False

pygame.quit()


