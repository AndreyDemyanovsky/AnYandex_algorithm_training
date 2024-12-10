n, a, b, w, h = map(int, input().split())

max_side = max(w, h)
min_side = min(w, h)


def get_count_moduls(size_protection):
    v1 = max_side // (max(a, b) + 2 * size_protection) * (min_side // (min(a, b) + 2 * size_protection))
    v2 = max_side // (min(a, b) + 2 * size_protection) * (min_side // (max(a, b) + 2 * size_protection))

    return max(v1, v2)


def search_thickness(l, r):
    while l < r:
        mid = (l + r + 1) // 2
        count_moduls = get_count_moduls(mid)
        if count_moduls < n:
            r = mid - 1
        else:
            l = mid
    return l


print(search_thickness(0, (10**18-2) // 2))