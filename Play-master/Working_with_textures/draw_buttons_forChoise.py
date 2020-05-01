from Working_with_textures.draw_button import draw_button


def draw_some_buttons(window, count: int, names: list, paper_size: tuple):
    answer = []
    for number in range(count):
        draw_button(window, (128, 0, 0),
                    (paper_size[0] + 20,
                     paper_size[1] + 20 + 10 * number + number *
                     (paper_size[3] - 40 - 10 * (count - 1)) // count,
                     paper_size[2] - 40,
                     (paper_size[3] - 40 - 10 * (count - 1)) // count),
                    names[number])
        answer += [(paper_size[0] + 20,
                    paper_size[1] + 20 + 10 * number + number *
                    (paper_size[3] - 40 - 10 * (count - 1)) // count,
                    paper_size[2] - 40,
                    (paper_size[3] - 40 - 10 * (count - 1)) // count)]
    return answer
