def left_binsearch(l, r, sequence, x):
    while l < r:
        mid = (l + r) // 2
        if sequence[mid] >= x:
            r = mid
        else:
            l = mid + 1

    return l


def right_binsearch(l, r, sequence, x):
    while l < r:
        mid = (l + r + 1) // 2
        if sequence[mid] <= x:
            l = mid
        else:
            r = mid - 1

    if sequence[l] > x:
        return -1
    return l


N = int(input())
lst = list(map(int, input().split()))
lst.sort()
result = []

k = int(input())  # кол запросов
for _ in range(k):
    left, right = map(int, input().split())
    r = right_binsearch(0, N - 1, lst, right)
    l = left_binsearch(0, N, lst, left)
    result.append(r - l + 1)

print(*result)
