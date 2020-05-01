import pygame


def draw_button(window, colour: tuple, coordinates: tuple, name: str = "",
                text_1=218, text_2=165, text_3=32, size=35):
    """
    :param size:
    :param text_1:
    :param text_2:
    :param text_3:
    :param font: Font of text
    :param colour: background colour
    :param coordinates: where should button be placed
    :param name: Button name
    :return: None
    Prints button in correct place
    """
    pygame.draw.rect(window, colour,
                     (coordinates[0],
                      coordinates[1],
                      coordinates[2],
                      coordinates[3]))
    fond = pygame.font.Font(None, size)
    text = fond.render(name, True, [text_1, text_2, text_3])
    window.blit(text, [coordinates[0] + coordinates[2] // 100 + 1, coordinates[
        1] + coordinates[3] // 100 + 1])
