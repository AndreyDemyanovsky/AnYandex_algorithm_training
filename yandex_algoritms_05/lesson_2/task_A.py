k = int(input())


def f(n, old_n, min_or_max="max"):
    if min_or_max == "max":
        return n if n > old_n else old_n
    return n if n < old_n else old_n


max_y, max_x = 0, 0
min_y, min_x = 10**9 + 1, 10**9 + 1
for _ in range(k):
    y, x = map(int, input().split())
    max_y = f(y, max_y,)
    max_x = f(x, max_x,)
    min_y = f(y, min_y, "min")
    min_x = f(x, min_x, "min")

print(min_y, min_x, max_y, max_x)