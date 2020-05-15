import pygame


def wait_klick(button_list, length, width):
    size = width - width // 4
    size_of_cell = size // 11
    click = None
    while click is None:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x1 = pos[0]
                mouse_y1 = pos[1]
                if button_list[1][0] + button_list[1][2] >= mouse_x1 >= [1][
                    0] and button_list[1][1] + button_list[1][3] >= mouse_y1\
                        >= button_list[1][1]:
                    return "Exit"
                elif button_list[0][0] + button_list[0][2] >= mouse_x1 >= \
                        button_list[0][0] and button_list[0][1] + \
                        button_list[0][3] >= mouse_y1 >= button_list[0][1]:
                    return "end"
                elif mouse_y1 <= width * 3 // 4:
                    print("Look here")
                    print(mouse_x1 // (length // 21), mouse_y1 // size_of_cell)
                    return "move " + str(mouse_x1 // (length // 21)) + " " + \
                           str(mouse_y1 // size_of_cell)
