borders = [[[0, 9], [0, 1]], [[0, 9], [10, 11]]]


def in_borders(coordinates, board=True, first_army_turn=True):
    if board:
        return 0 <= coordinates[0] <= 9 and 0 <= coordinates[1] <= 11
    elif first_army_turn:
        return 0 <= coordinates[0] <= 9 and 0 <= coordinates[1] <= 1
    else:
        return 0 <= coordinates[0] <= 9 and 10 <= coordinates[1] <= 11
