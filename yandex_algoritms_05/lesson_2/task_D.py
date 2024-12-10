N = int(input())


def getPer(yx, modifier=None, mod=None):
    if 0 <= modifier <= 7:
        if mod == "x":
            if d[yx][modifier] == 1:
                return -1
        elif mod == "y":
            if d[modifier][yx] == 1:
                return -1
    return 1


d = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]


perimeter = 0
for _ in range(N):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    d[y][x] = 1
    low = y - 1
    top = y + 1
    right = x + 1
    left = x - 1

    perimeter += getPer(x, top, "y")
    perimeter += getPer(x, low, "y")
    perimeter += getPer(y, right, "x")
    perimeter += getPer(y, left, "x")


print(perimeter)
