import pygame

pygame.init()

from Working_with_textures.draw_some_buttons import draw_some_buttons
from Working_with_textures.NewField import create_window_of_Field


def choose_units_to_kill(window, fullscreen, units):
    window = create_window_of_Field(window, fullscreen, "Field")
    pygame.display.update()
    if len(units) > 4:
        buttons = draw_some_buttons(window, 4,
                                    [units[0].base.name, units[1].base.name,
                                     units[2].base.name, units[3].base.name],
                                    (0, 0, 100, 200),
                                    255, 215, 0, 85, 107, 47, 10)
        names = []
        for i in units[4:]:
            names += [i.base.name]
        buttons += draw_some_buttons(window, len(names), names,
                                     (700, 0, 100, 150),
                                     255, 215, 0, 85, 107, 47, 10)
    else:
        names = []
        for i in units:
            names += [i.base.name]
        buttons = draw_some_buttons(window, len(names),
                                    names,
                                    (0, 0, 100, 200),
                                    255, 215, 0, 85, 107, 47, 10)

    buttons += draw_some_buttons(window, 1, ["End"],
                                 (700, 150, 100, 75),
                                 255, 215, 0, 85, 107, 47,
                                 15)
    pygame.display.update()
    return buttons
