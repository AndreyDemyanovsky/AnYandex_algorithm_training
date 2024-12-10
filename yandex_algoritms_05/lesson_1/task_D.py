N = 8
pole = []
for _ in range(N):
    row = list(input())
    pole.append(row)


del_cords = set()


def is_in_range_and_not_figure(y, x):
    in_range = 0 <= y <= 7 and 0 <= x <= 7
    is_not_figure = False
    if in_range:
        is_not_figure = pole[y][x] not in "RB"
    return in_range and is_not_figure


def get_new_coord(i, j, value_i, valuer_j):
    return i + value_i, j + valuer_j


def rook(i, j):

    top = (i - 1, j)
    bottom = (i + 1, j)
    left = (i, j - 1)
    right = (i, j + 1)

    while True:
        if is_in_range_and_not_figure(*top):
            del_cords.add(top)
            top = top[0] - 1, j
        elif is_in_range_and_not_figure(*bottom):
            del_cords.add(bottom)
            bottom = bottom[0] + 1, j
        elif is_in_range_and_not_figure(*left):
            del_cords.add(left)
            left = i, left[1] - 1
        elif is_in_range_and_not_figure(*right):
            del_cords.add(right)
            right = i, right[1] + 1
        else:
            break


def elephant(i, j):

    left_top = (i - 1, j - 1)
    right_top = (i - 1, j + 1)
    left_bottom = (i + 1, j - 1)
    right_bottom = (i + 1, j + 1)

    while True:
        if is_in_range_and_not_figure(*left_top):
            del_cords.add(left_top)
            left_top = get_new_coord(*left_top, -1, -1)

        elif is_in_range_and_not_figure(*left_bottom):
            del_cords.add(left_bottom)
            left_bottom = get_new_coord(*left_bottom, 1, -1)

        elif is_in_range_and_not_figure(*right_top):
            del_cords.add(right_top)
            right_top = get_new_coord(*right_top, -1, 1)

        elif is_in_range_and_not_figure(*right_bottom):
            del_cords.add(right_bottom)
            right_bottom = get_new_coord(*right_bottom, 1, 1)
        else:
            break


for i in range(8):
    for j in range(8):
        if pole[i][j] == "R":
            del_cords.add((i, j))
            rook(i, j)
        if pole[i][j] == "B":
            del_cords.add((i, j))
            elephant(i, j)

print(64 - len(del_cords))