n_copy, x_pages, y_pages = map(int, input().split())

mi = min(x_pages, y_pages)
mx = max(x_pages, y_pages)


def check(sec):
    p = 0
    sec -= mi
    if sec >= 0:
        p = 1
        p += sec // mx + sec // mi
    return p


def search(l, r):
    while l < r:
        sec = (l + r) // 2
        if check(sec) >= n_copy:
            r = sec
        else:
            l = sec + 1
    return l


print(search(0, (2 * 10**8) * 10))

