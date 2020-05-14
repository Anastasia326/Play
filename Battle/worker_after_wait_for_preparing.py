def worker_after_wait_for_preparing(click1, click2, mouse_x1, mouse_y1,
                                    mouse_x2, mouse_y2, length=800, higth=600):
    size_of_cell = (higth * 5 // 6) // 10
    size = (length - size_of_cell * 12) // 2
    if click1 == 2 and click2 == 1:
        first_unit = mouse_y1 // size_of_cell + (
                    mouse_y1 % size_of_cell > 0) - 1 + \
                     4 * (length >= mouse_x1 >= length - size)
        cell_x = (mouse_x2 - size) // size_of_cell
        cell_y = mouse_y2 // size_of_cell
        return "stash " + str(first_unit) + " " + str(cell_y) + " " + str(
            cell_x), ""
    elif click1 == 1 and click2 == 2:
        cell_x = (mouse_x1 - size) // size_of_cell
        cell_y = mouse_y1 // size_of_cell
        return "move " + str(cell_y) + " " + str(cell_x) + " stash", ""
    elif click1 == 2 and click2 == 2:
        return "Nothing happened", "Nothing happened"
    elif click1 == 1 and click2 == 1:
        cell_x1 = (mouse_x1 - size) // size_of_cell
        cell_y1 = mouse_y1 // size_of_cell
        cell_x2 = (mouse_x2 - size) // size_of_cell
        cell_y2 = mouse_y2 // size_of_cell
        return "move " + str(cell_y1) + " " + str(cell_x1) + " to " + str(
            cell_y2) + " " + str(cell_x2), ""
    elif click1 == 3 and click2 == 3:
        return "end", ""
    elif (higth >= mouse_y1 >= higth * 11 // 12
        and length >= mouse_x1 >= length * 7 // 8) or (
            higth >= mouse_y2 >= higth * 11 // 12
            and length >= mouse_x2 >= length * 7 // 8):
        return "EXIT", ""
    elif click1 == 4:
        return "EXIT", ""
