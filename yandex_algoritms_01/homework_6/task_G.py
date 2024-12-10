n = int(input())
m = int(input())
num_tail = int(input())


def check(width):
    var = (n - width * 2)
    var2 = (m - width * 2)
    if var < 1 or var2 < 1:
        return n * m + 1
    return n * m - var * var2


def search(l, r):
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid) <= num_tail:
            l = mid
        else:
            r = mid - 1
    return l


print(search(0, min(n, m) - 1))
