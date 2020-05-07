def button_was_clicked(buttons: list,
                       move_to_page: list,
                       mouse_position: list):
    """
    :param mouse_position: x and t coordinates in click
    :param buttons: what buttons are on screen now
    :param move_to_page: what pages will be next
    :return: was it clicked or not, index of button and next page name
    """
    for button in buttons:
        if button[0] < mouse_position[0] < button[0] + button[2] and \
                button[1] < mouse_position[1] < button[1] + button[3]:
            return [True,
                    move_to_page[buttons.index(button)]]
    return [False, None]
