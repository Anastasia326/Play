def worker_after_wait_for_preparing(wait, click1, click2, mouse_x1, mouse_y1,
                                    mouse_x2, mouse_y2, units, window, length = 800, higth = 600):
    if click1 == 2 and click2 == 1:
        first_unit = mouse_y1//50 + (mouse_y1 % 50 > 0) - 1 + \
                     4 * (800 >= mouse_x1 >= 650)
        cell_x = (mouse_x2 - 100) // 50
        cell_y = (mouse_y2 - 2) // 50
        return "stash " + str(first_unit) + " " + str(cell_y) + " " + str(
            cell_x), ""
    if click1 == 1 and click2 == 2:
        cell_x = (mouse_x1 - 100) // 50
        cell_y = (mouse_y1 - 2) // 50
        return "move " + str(cell_y) + " " + str(cell_x) + " stash", ""
    if click1 == 2 and click2 == 2:
        return "Nothing happened", "Nothing happened"
    if click1 == 1 and click2 == 1:
        cell_x1 = (mouse_x1 - 100) // 50
        cell_y1 = (mouse_y1 - 2) // 50
        cell_x2 = (mouse_x2 - 100) // 50
        cell_y2 = (mouse_y2 - 2) // 50
        return "move " + str(cell_y1) + " " + str(cell_x1) + " to " + str(
            cell_y2) + " " + str(cell_x2), ""
    if click1 == 3 and click2 == 3:
        return "end", ""
    if (higth >= mouse_y1 >= higth * 11 // 12
        and length >= mouse_x1 >= length * 7 // 8) or (
            higth >= mouse_y2 >= higth * 11 // 12
            and length >= mouse_x2 >= length * 7 // 8):
        return "EXIT", ""
    if click1 == 4:
        return "EXIT", ""
