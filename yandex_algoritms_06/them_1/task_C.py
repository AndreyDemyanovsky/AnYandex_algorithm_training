N = int(input())
data = [list(input()) for _ in range(N)]


def delete_void_row(display):
    first_row_with_diode = None
    last_row_with_diode = None
    for i, v in enumerate(display):
        if "#" in set(v):
            if first_row_with_diode is None:
                first_row_with_diode = i
            last_row_with_diode = i

    if first_row_with_diode is None:
        last_row_with_diode =first_row_with_diode = 0

    return display[first_row_with_diode:last_row_with_diode + 1]


def compress(display):
    result = []
    for i in range(len(display)):
        if not result:
            result.append(display[i])
        else:
            if display[i] != result[-1]:
                result.append(display[i])
    return result

display_without_void_row = delete_void_row(data)
transposed_display = list(zip(*display_without_void_row))
display_without_void_column = delete_void_row(transposed_display)
display = list(zip(*display_without_void_column))

compress_row = compress(display)
compress_column = compress(list(zip(*compress_row)))
letter = [list(i) for i in zip(*compress_column)]

if letter == [["#"]]:
    print("I")
elif letter == [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]]:
    print("O")
elif letter == [["#", "#"], ["#", "."], ["#", "#"]]:
    print("C")
elif letter == [["#", ".", "#"], ["#", "#", "#"], ["#", ".", "#"]]:
    print("H")
elif letter == [["#", "."], ["#", "#"]]:
    print("L")
elif letter == [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"], ["#", ".", "."]]:
    print("P")
else:
    print("X")
