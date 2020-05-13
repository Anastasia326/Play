def worker_after_wait_for_preparing(wait, click1, click2, mouse_x1, mouse_y1,
                                    mouse_x2, mouse_y2, units, window):
    if click1 == 2 and click2 == 1:
        first_unit = mouse_y1//50 + (mouse_y1 % 50 > 0) - 1 + \
                     4 * (800 >= mouse_x1 >= 650)
        cell_x = (mouse_x2 - 100) // 50
        cell_y = (mouse_y2 - 2) // 50
        return "stash " + str(first_unit) + " " + str(cell_y) + " " + str(
            cell_x)
    if click1 == 1 and click2 == 2:
        cell_x = (mouse_x1 - 50) // 12
        cell_y = (mouse_y1 - 2) // 10
        return "move " + str(cell_y) + " " + str(cell_x) + "stash"
    if click1 == 1 and click2 == 1:
        return "Nothing happened"
    if click1 == 2 and click2 == 2:
        cell_x1 = (mouse_x1 - 50) // 12
        cell_y1 = (mouse_y1 - 2) // 10
        cell_x2 = (mouse_x2 - 50) // 12
        cell_y2 = (mouse_y2 - 2) // 10
        return "move " + str(cell_y1) + " " + str(cell_x1) + " " + str(
            cell_y2) + " " + str(cell_x2)
    if click1 == 3 and click2 == 3:
        return "end"
