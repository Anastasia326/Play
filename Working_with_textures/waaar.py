import pygame

from Working_with_textures.was_clicked import button_was_clicked


def waaar(button_list, commands):
    run = True
    string = ""
    new_click = False
    while run:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if not new_click:
                    yes, names = button_was_clicked(button_list, commands, pos)
                    if yes:
                        if names == "Wait":
                            return "wait"
                        elif names == "Defend":
                            return "defend"
                        elif names == "Exit":
                            return "exit"
                        else:
                            string += names
                            string += " "
                            new_click = True
                else:
                    x = (pos[0] - 100) // 50
                    y = (pos[1] - 2) // 50
                    if string != "move_attack ":
                        return string + str(y) + " " + str(x)
                    elif len(string.split()) < 3:
                        string += str(y) + " " + str(x) + " "
                    else:
                        return string + str(y) + " " + str(x)
