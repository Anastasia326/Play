import pygame


def draw_button(window, colour: tuple, coordinates: tuple, name: str,
                font: int = 40):
    """
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
    fond = pygame.font.Font(None, 35)
    text = fond.render(name, True, [218, 165, 32])
    window.blit(text, [coordinates[0] + coordinates[2] // 100 + 1, coordinates[
        1] + coordinates[3] // 100 + 1])
