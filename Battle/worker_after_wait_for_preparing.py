import pygame
from Battle.wait import wait

def worker_after_wait_for_preparing(wait, click1, click2, mouse_x1, mouse_y1, mouse_x2, mouse_y2, units, window):
    first_unit = 0
    cell_x = 0
    cell_y = 0
    print(mouse_x2, mouse_y2)
    if click1 == 2 and click2 == 1:
        if 50 >= mouse_y1 >= 0 and   150 >= mouse_x1 >= 0:
            first_unit = 0
        if 100 >= mouse_y1 > 50 and   150 >= mouse_x1 >= 0:
            first_unit = 1
        if 150 >= mouse_y1 > 100 and   150 >= mouse_x1 >= 0:
            first_unit = 2
        if 200 >= mouse_y1 > 150 and   150 >= mouse_x1 >= 0:
            first_unit = 3
        if 50 >= mouse_y1 >= 0 and   800 >= mouse_x1 >= 650:
            first_unit = 4
        if 100 >= mouse_y1 > 50 and   800 >= mouse_x1 >= 650:
            first_unit = 5
        if 150 >= mouse_y1 > 100 and 800 >= mouse_x1 >= 650:
            first_unit = 6
        cell_x = (mouse_x2 - 100) // 50
        cell_y = (mouse_y2 - 2) // 50
        return "stash " + str(first_unit) + " " + str(cell_y) + " " + str(cell_x)
    if click1 == 1 and click2 == 2:
        if 50 >= mouse_y2 >= 0 and   150 >= mouse_x2 >= 0:
            first_unit = 0
        if 100 >= mouse_y2 > 50 and   150 >= mouse_x2 >= 0:
            first_unit = 1
        if 150 >= mouse_y2 > 100 and   150 >= mouse_x2 >= 0:
            first_unit = 2
        if 200 >= mouse_y2 > 150 and   150 >= mouse_x2 >= 0:
            first_unit = 3
        if 50 >= mouse_y2 >= 0 and   800 >= mouse_x2 >= 650:
            first_unit = 4
        if 100 >= mouse_y2 > 50 and   800 >= mouse_x2 >= 650:
            first_unit = 5
        if 150 >= mouse_y2 > 100 and 800 >= mouse_x2 >= 650:
            first_unit = 6
        cell_x = (mouse_x1 - 50) // 12
        cell_y = (mouse_y1 - 2) // 10
        return "move " + str(cell_y) + " " + str(cell_x) + "stash"
    if click1 == 2 and click2 == 2:
        cell_x1 = (mouse_x1 - 50) // 12
        cell_y1 = (mouse_y1 - 2) // 10
        cell_x2 = (mouse_x2 - 50) // 12
        cell_y2 = (mouse_y2 - 2) // 10
        return "move " + str(cell_y1) + " " + str(cell_x1) + " " + str(cell_y2) + " " + str(cell_x2)
    if click1 == 3 and click2 == 3:
        return  "end"
