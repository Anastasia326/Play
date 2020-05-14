import pygame

from Battle.Battle_ import Battle
from Battle.borders import army_list
from Modes.Play import Play
from Working_with_textures.NewField import create_window_of_Field
from Working_with_textures.arrays import heroes_list, classes_list
from Working_with_textures.chose_with_whom_play import chose_with_whom_play
from Working_with_textures.end_of_game import end_of_game
from Working_with_textures.was_clicked import button_was_clicked
from Working_with_textures.window_with_choise import create_window_choise


def Start_Battle(window, fullscreen, mode:str):
    run = True
    buttons_list = []
    what_happened = "Choise"
    window = create_window_of_Field(window, fullscreen, "Field")
    pygame.draw.line(window, (90, 90, 255), (10, 100), (20, 50))
    i = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    a = True
    start = 0
    first_army = None
    second_army = None
    while run:
        pygame.time.delay(1)
        i += 1
        if i == 120000:
            run = False
        x = 10
        clock = pygame.time.Clock()
        while x <= 840 and a:
            font = pygame.font.SysFont('dejavuserif', 60)
            text = font.render("Let the battle begin!", True, (255, 215, 0))
            clock.tick(60)
            window = create_window_of_Field(window, fullscreen, "Field")
            window.blit(text, (x, 250))
            x += 30
            pygame.display.update()
        a = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if what_happened == "Choise":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    was_clicked, buttons_list = create_window_choise(window,
                                                                     fullscreen)
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(buttons_list,
                                                                classes_list,
                                                                [mouse_x,
                                                                 mouse_y])
                    if next_page is not None:
                        what_happened = next_page
                        index_ = classes_list.index(what_happened)
                        buttons_list = chose_with_whom_play(
                            window,
                            fullscreen,
                            heroes_list[index_][0],
                            heroes_list[index_][1]
                        )

                    print(next_page, what_happened)
            elif what_happened in classes_list:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(
                        buttons_list,
                        heroes_list[classes_list.index(what_happened)],
                        [mouse_x, mouse_y]
                    )
                    if was_clicked:
                        start += 1
                        if start == 1:
                            first_army = army_list[
                                classes_list.index(what_happened)
                            ][
                                heroes_list[classes_list.index(
                                    what_happened)].index(next_page)
                            ]
                            what_happened = "Choise"
                        elif start == 2:
                            second_army = army_list[
                                classes_list.index(what_happened)
                            ][
                                heroes_list[classes_list.index(
                                    what_happened)].index(next_page)
                            ]
                            what_happened = "Set up the army"
            elif what_happened == "Set up the army":
                if mode == "Duel":
                    battle = Battle(first_army, second_army, window, fullscreen)
                else:
                    Play(first_army, second_army, mode, window, fullscreen)
                what_happened = "End"
            elif what_happened == "End":
                buttons_list = end_of_game(window, fullscreen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    mouse_x, mouse_y = pos[0], pos[1]
                    was_clicked, next_page = button_was_clicked(
                        buttons_list, ["Exit"], [mouse_x, mouse_y])
                    if was_clicked:
                        what_happened = next_page
            elif what_happened == "Exit":
                run = False
