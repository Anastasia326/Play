import pygame

from Working_with_textures.was_clicked import button_was_clicked


def wait_klick(button_list, length, width):
    click = None
    while click is None:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x1 = pos[0]
                mouse_y1 = pos[1]
                print(mouse_y1, width - (width // 3) + 10)
                if button_list[1][0] + button_list[1][2] >= mouse_x1 >= [1][0] and button_list[1][1] + button_list[1][
                    3] >= mouse_y1 >= button_list[1][1]:
                    return "Exit"
                elif button_list[0][0] + button_list[0][2] >= mouse_x1 >= button_list[0][0] and button_list[0][
                    1] + button_list[0][3] >= mouse_y1 >= button_list[0][1]:
                    return "end"
                elif mouse_y1 <= width * 3 // 4:
                    return "move " + str(mouse_x1 // (length // 21)) + " " + \
                           str(mouse_y1 // (length // 21))
