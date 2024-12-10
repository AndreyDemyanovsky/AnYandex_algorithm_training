count_row, count_column, count_min = map(int, input().split())
pole = [[0] * count_column for i in range(count_row)]


def counting_mines(r_min, c_min, pole):
    coords_check = ((-1, -1), (-1, 0), (0, -1), (1, 1), (1, 0), (0, 1), (1, -1), (-1, 1))

    for r, c in coords_check:
        if 0 <= r + r_min <= count_row - 1 and 0 <= c + c_min <= count_column - 1:
            if pole[r + r_min][c + c_min] != "*":
                pole[r + r_min][c + c_min] += 1


for i in range(count_min):
    row_min, column_min = map(lambda x: int(x) - 1, input().split())
    pole[row_min][column_min] = "*"
    counting_mines(row_min, column_min, pole)


for i in pole:
    print(*i)
        
