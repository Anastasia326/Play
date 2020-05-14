import pygame

from Working_with_textures.was_clicked import button_was_clicked


def wait(button_list, width, height, k):
    click1 = None
    click2 = None
    mouse_x1 = 0
    mouse_y1 = 0
    mouse_x2 = 0
    mouse_y2 = 0
    size_of_cell = (height * 5 // 6) // 10
    size = (width - size_of_cell * 12) // 2
    first_click = True
    while click1 is None or click2 is None:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if width - size >= pos[0] >= size and size_of_cell * 10 >= pos[1] >= 0:
                    if first_click:
                        mouse_x1, mouse_y1 = pos[0], pos[1]
                        click1 = 1  # на полe
                        first_click = False
                    else:
                        mouse_x2, mouse_y2 = pos[0], pos[1]
                        click2 = 1
                elif width >= pos[0] > width - size and size_of_cell * 4 + 10 <= pos[1] <= size_of_cell * 4 + 10 + int(
                        75 * k):
                    click1 = 3
                    click2 = 3
                elif width >= pos[0] >= width - size and height >= pos[1] >= height - int(75 * k):
                    click1 = 4
                    click2 = 4
                else:
                    click, n = button_was_clicked(button_list,
                                                  [""]*7,
                                                  [pos[0],
                                                   pos[1]])
                    if click:
                        if first_click:
                            mouse_x1, mouse_y1 = pos[0], pos[1]
                            click1 = 2
                            first_click = False
                        else:
                            mouse_x2, mouse_y2 = pos[0], pos[1]
                            click2 = 2
    return True, click1, click2, mouse_x1, mouse_y1, mouse_x2, mouse_y2
