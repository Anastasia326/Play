from Working_with_textures.draw_button import draw_button


def draw_button2(window, colour: tuple, coordinates: tuple, names: str = "",
                 text_1=218, text_2=165, text_3=32, size=35):
    answer = []
    draw_button(window, colour, coordinates, names, text_1, text_2, text_3,
                size)
    answer += [(coordinates[0],
                coordinates[1],
                coordinates[2],
                coordinates[3])]
    return answer
