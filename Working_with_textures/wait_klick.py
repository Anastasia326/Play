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
                if length - 2 * (
                        length // 10) >= mouse_x1 - length // 10 >= 0 and width // 10 * 3 + width // 6 * 4 + 10 >= mouse_y1 >= width // 6 * 4 + 10 + width // 20 * 3:
                    return "end"
                elif length - 2 * (
                        length // 10) >= mouse_x1 - length // 10 >= 0 and width // 20 * 3 >= mouse_y1 - width // 6 * 4 + 10 >= 0:
                    return "Exit"
                elif mouse_y1 <= width - (width // 3 + 10):
                    return "move " + str(mouse_x1 // (length // 21)) + " "+ \
                           str(mouse_y1 // (length // 21))
