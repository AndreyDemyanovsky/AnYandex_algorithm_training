def get_count_busy_call(k):
    res = 0
    for i in range(1, k + 1):
        res += (k + 1) * i
        k -= 1
    return res - 1


def binsearch(l, r):
    while l < r:
        mid = (l + r + 1) // 2
        x = get_count_busy_call(mid)

        if x <= N:
            l = mid
        else:
            r = mid - 1
    return l


N = int(input())
print(binsearch(0, 1_900_000))