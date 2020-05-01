from Working_with_textures.draw_button import draw_button


def draw_some_buttons(window, count: int, names: list, paper_size: tuple,
                      color1=128, color2=0, color3=0, text_1=218, text_2=165,
                      text_3=32, size=35):
    """
    :param window: window on what to put
    :param count: Count of buttons that should be drawn
    :param names: list of names of buttons
    :param paper_size: size of menu
    :return: coordinats of all buttons
    """
    answer = []
    for number in range(count):
        draw_button(window, (color1, color2, color3),
                    (paper_size[0] + 20,
                     paper_size[1] + 20 + 10 * number + number *
                     (paper_size[3] - 40 - 10 * (count - 1)) // count,
                     paper_size[2] - 40,
                     (paper_size[3] - 40 - 10 * (count - 1)) // count),
                    names[number], text_1, text_2, text_3, size)
        answer += [(paper_size[0] + 20,
                    paper_size[1] + 20 + 10 * number + number *
                    (paper_size[3] - 40 - 10 * (count - 1)) // count,
                    paper_size[2] - 40,
                    (paper_size[3] - 40 - 10 * (count - 1)) // count)]
    return answer
