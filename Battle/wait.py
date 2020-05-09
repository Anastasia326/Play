import pygame

pygame.init()

from Working_with_textures.was_clicked import button_was_clicked


def wait(button_list):
    click1 = None
    click2 = None
    mouse_x1 = 0
    mouse_y1 = 0
    mouse_x2 = 0
    mouse_y2 = 0
    first_click = True
    while click1 is None or click2 is None:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if 700 >= pos[0] >= 100 and 500 >= pos[1] >= 0:
                    if first_click:
                        mouse_x1, mouse_y1 = pos[0], pos[1]
                        click1 = 1  # на полe
                        first_click = False
                    else:
                        mouse_x2, mouse_y2 = pos[0], pos[1]
                        click2 = 1
                elif 800 >= pos[0] > 700 and 150 >= pos[1] >= 100:
                    click1 = 3
                    click2 = 3
                else:
                    click, n = button_was_clicked(button_list, [""] * 7,
                                                  [pos[0], pos[1]])
                    if click:
                        if first_click:
                            mouse_x1, mouse_y1 = pos[0], pos[1]
                            click1 = 2
                            first_click = False
                        else:
                            mouse_x2, mouse_y2 = pos[0], pos[1]
                            click2 = 2
    return True, click1, click2, mouse_x1, mouse_y1, mouse_x2, mouse_y2
