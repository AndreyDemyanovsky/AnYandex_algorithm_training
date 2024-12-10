number_regiments, number_reconnaissance = map(int, input().split())
army = list(map(int, input().split()))


def get_pref_sum(lst):
    pref = []
    for i in range(len(lst) + 1):
        if not pref:
            pref.append(0)
        else:
            pref.append(lst[i - 1] + pref[i - 1])
    return pref


prefix = get_pref_sum(army)


def get_sum_in_window(s, e):
    return prefix[e] - prefix[s]


def bin_search(l, r, target):
    while l < r:
        mid = (l + r) // 2
        if get_sum_in_window(mid, mid + size_window) >= target:
            r = mid
        else:
            l = mid + 1

    if get_sum_in_window(l, l + size_window) != target:
        return -1
    return l


res = []
for _ in range(number_reconnaissance):
    size_window, target = map(int, input().split())
    ans = bin_search(0, len(army) - size_window, target)
    if ans != -1:
        ans += 1
    res.append(ans)


print(*res, sep="\n")