number_of_races, number_of_classes = map(int, input().split())

all_characters = []
for i in range(number_of_races):
    all_characters.append(list(map(int, input().split())))


def find_max(matrix, ban_row=None, ban_col=None, return_row_column=False):
    res = -1
    row_res = col_res = None

    for rw in range(number_of_races):
        if rw != ban_row:
            for cl in range(number_of_classes):
                if cl != ban_col:
                    mx = matrix[rw][cl]
                    if mx > res:
                        res = mx
                        row_res = rw
                        col_res = cl

    return res if not return_row_column else res, row_res, col_res


first_max, row_first_max, column_first_max = find_max(all_characters, return_row_column=True)


second_max_with_banrow, *row_col = find_max(all_characters, ban_row=row_first_max)
res1_after_banrowcol = find_max(all_characters, row_first_max, row_col[1])

second_max_with_bancol, *row_col2 = find_max(all_characters, ban_col=column_first_max)
res2_after_bancolrow = find_max(all_characters, row_col2[0], column_first_max)

if res1_after_banrowcol < res2_after_bancolrow:
    print(row_first_max + 1, row_col[1] + 1)
else:
    print(row_col2[0] + 1, column_first_max + 1)