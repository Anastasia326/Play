import pygame

from Working_with_textures.arrays import simple_buttons
from Working_with_textures.was_clicked import button_was_clicked


def waaar(button_list, commands, width, hight):
    run = True
    string = ""
    new_click = False
    size_cell = (hight * 5 // 6) // 10
    size = (width - size_cell * 12) // 2
    while run:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if width >= pos[0] >= width * 7 // 8 and hight >= pos[1] >= hight - size_cell:
                    return "EXIT"
                if not new_click:
                    yes, names = button_was_clicked(button_list, commands, pos)
                    if yes:
                        if names in simple_buttons:
                            return names.lower()
                        else:
                            string += names
                            string += " "
                            new_click = True
                else:
                    x = (pos[0] - size) // size_cell
                    print(x)
                    print((pos[0] - size) // size_cell)
                    y = (pos[1]) // size_cell
                    print(y)
                    print((pos[1] - 2) // 50)
                    if string != "move_attack ":
                        return string + str(y) + " " + str(x)
                    elif len(string.split()) < 3:
                        string += str(y) + " " + str(x) + " "
                    else:
                        return string + str(y) + " " + str(x)
