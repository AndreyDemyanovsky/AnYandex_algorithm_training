w, h, n = map(int, input().split())


def check(size_sq):
    ww = size_sq // w
    hh = size_sq // h
    return ww * hh


def bin_search(l, r):
    while l < r:
        mid = (l + r) // 2
        res_check = check(mid)
        if res_check >= n:
            r = mid
        else:
            l = mid + 1
    return l


print(bin_search(1, 32000 * 10**9))