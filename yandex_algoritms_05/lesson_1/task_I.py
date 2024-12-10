N = int(input())

ships = []
for _ in range(N):
    i, j = map(int, input().split())
    ships.append((i - 1, j - 1))

ships.sort()

def get_count_cell(new_i, new_j):
    if new_i < 0:
        new_i *= - 1
    if new_j < 0:
        new_j *= - 1
    return new_i + new_j


min_path = None
for column in range(N):
    all_path = 0
    for i in range(N):
        ship = ships[i]
        row = i
        all_path += get_count_cell(ship[0] - row, ship[1] - column)

    if min_path is not None:
        min_path = min(min_path, all_path)
    else:
        min_path = all_path

print(min_path)