import pygame

window = None


def create_window(length: int, width: int, fullscreen=False):
    infoObject = pygame.display.Info()
    print(infoObject.current_w, length, infoObject.current_h, width)
    if infoObject.current_w < length or infoObject.current_h < width:
        print("you can't choose that. Default was set")
        length = 800
        width = 480
    global window
    if length == 800 and width == 480:
        background_image = pygame.image.load(
            "gory-zamok-krepost-reka-most.jpg")
        if fullscreen:
            window = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)
        else:
            window = pygame.display.set_mode((800, 480))
        window.blit(background_image, [0, 0])
        pygame.display.set_caption("Герои меча и магии -1")

        background_menu = pygame.draw.rect(window, (205, 133, 63),
                                           (310, 160, 240, 160))
        start_button = pygame.draw.rect(window, (128, 0, 0),
                                        (330, 168, 200, 28))
        settings_button = pygame.draw.rect(window, (128, 0, 0),
                                           (330, 206, 200, 28))
        info_button = pygame.draw.rect(window, (128, 0, 0),
                                       (330, 244, 200, 28))
        quit_button = pygame.draw.rect(window, (128, 0, 0),
                                       (330, 282, 200, 28))
        pygame.display.update()
        return [(330, 168, 200, 28),
                (330, 206, 200, 28),
                (330, 244, 200, 28),
                (330, 282, 200, 28)]
    elif length == 1600 and width == 800:
        if fullscreen:
            window = pygame.display.set_mode((1600, 800), pygame.FULLSCREEN)
        else:
            window = pygame.display.set_mode((1600, 800))
        background_image = pygame.image.load("1600x800.jpg")
        window.blit(background_image, [0, 0])
        pygame.display.set_caption("Герои меча и магии -1")

        background_menu = pygame.draw.rect(window, (205, 133, 63),
                                           (500, 300, 380, 230))
        start_button = pygame.draw.rect(window, (128, 0, 0),
                                        (530, 321, 320, 40))
        settings_button = pygame.draw.rect(window, (128, 0, 0),
                                           (530, 372, 320, 40))
        info_button = pygame.draw.rect(window, (128, 0, 0),
                                       (530, 423, 320, 40))
        quit_button = pygame.draw.rect(window, (128, 0, 0),
                                       (530, 474, 320, 40))
        pygame.display.update()
        return [(530, 321, 320, 40),
                (530, 372, 320, 40),
                (530, 423, 320, 40),
                (530, 474, 320, 40)]
    elif length == 1920 and width == 1080:
        background_image = pygame.image.load("1920x1080.jpg")
        if fullscreen:
            window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        else:
            window = pygame.display.set_mode((1920, 1080))
        window.blit(background_image, [0, 0])
        pygame.display.set_caption("Герои меча и магии -1")

        background_menu = pygame.draw.rect(window, (205, 133, 63),
                                           (500, 300, 380, 230))
        start_button = pygame.draw.rect(window, (128, 0, 0),
                                        (530, 321, 320, 40))
        settings_button = pygame.draw.rect(window, (128, 0, 0),
                                           (530, 372, 320, 40))
        info_button = pygame.draw.rect(window, (128, 0, 0),
                                       (530, 423, 320, 40))
        quit_button = pygame.draw.rect(window, (128, 0, 0),
                                       (530, 474, 320, 40))
        pygame.display.update()
        return [(530, 321, 320, 40),
                (530, 372, 320, 40),
                (530, 423, 320, 40),
                (530, 474, 320, 40)]
    elif length == 1280 and width == 720:
        background_image = pygame.image.load("1280x720.jpg")
        if fullscreen:
            window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        else:
            window = pygame.display.set_mode((1280, 720))
        window.blit(background_image, [0, 0])
        pygame.display.set_caption("Герои меча и магии -1")

        background_menu = pygame.draw.rect(window, (205, 133, 63),
                                           (500, 300, 380, 230))
        start_button = pygame.draw.rect(window, (128, 0, 0),
                                        (530, 321, 320, 40))
        settings_button = pygame.draw.rect(window, (128, 0, 0),
                                           (530, 372, 320, 40))
        info_button = pygame.draw.rect(window, (128, 0, 0),
                                       (530, 423, 320, 40))
        quit_button = pygame.draw.rect(window, (128, 0, 0),
                                       (530, 474, 320, 40))
        pygame.display.update()
        return [(530, 321, 320, 40),
                (530, 372, 320, 40),
                (530, 423, 320, 40),
                (530, 474, 320, 40)]
    elif length == 1178 and width == 663:
        background_image = pygame.image.load("1178x663.jpg")
        if fullscreen:
            window = pygame.display.set_mode((1178, 663), pygame.FULLSCREEN)
        else:
            window = pygame.display.set_mode((1178, 663))
        window.blit(background_image, [0, 0])
        pygame.display.set_caption("Герои меча и магии -1")

        background_menu = pygame.draw.rect(window, (205, 133, 63),
                                           (500, 300, 380, 230))
        start_button = pygame.draw.rect(window, (128, 0, 0),
                                        (530, 321, 320, 40))
        settings_button = pygame.draw.rect(window, (128, 0, 0),
                                           (530, 372, 320, 40))
        info_button = pygame.draw.rect(window, (128, 0, 0),
                                       (530, 423, 320, 40))
        quit_button = pygame.draw.rect(window, (128, 0, 0),
                                       (530, 474, 320, 40))
        pygame.display.update()
        return [(530, 321, 320, 40),
                (530, 372, 320, 40),
                (530, 423, 320, 40),
                (530, 474, 320, 40)]


pygame.init()
buttons_list = create_window(1178, 663, True)
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        press = pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            mouse_x, mouse_y = pos[0], pos[1]
            if buttons_list[3][0] < mouse_x < buttons_list[3][0] + \
                    buttons_list[3][2] and buttons_list[3][1] < mouse_y \
                    < buttons_list[3][1] + buttons_list[3][3]:
                run = False
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
