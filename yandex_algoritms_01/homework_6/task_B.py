n, k = map(int, input().split())

list_num = list(map(int, input().split()))
to_find = list(map(int, input().split()))


def bin_search(left_border, right_border, lst, target):
    while left_border < right_border - 1:
        mid = (left_border + right_border + 1) // 2
        if lst[mid] <= target:
            left_border = mid
        else:
            right_border = mid

    return lst[left_border] if target - lst[left_border] <= lst[right_border] - target else lst[right_border]


for i in to_find:
    print(bin_search(0, n - 1, list_num, i))
