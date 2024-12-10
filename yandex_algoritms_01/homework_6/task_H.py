n, k = map(int, input().split())

ls = []
for _ in range(n):
    ls.append(int(input()))


def check(length):
    n_cut = 0
    for i in ls:
        n_cut += i // length
    return n_cut


def search(l, r, t):
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid) >= t:
            l = mid
        else:
            r = mid - 1
    return l


print(search(0, max(ls), k))