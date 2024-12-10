n, k = map(int, input().split())

list_num = list(map(int, input().split()))
to_find = list(map(int, input().split()))


def bin_search(left_border, right_border, lst, target):
    while left_border < right_border:
        mid = (left_border + right_border) // 2
        if lst[mid] >= target:
            right_border = mid
        else:
            left_border = mid + 1

    if lst[left_border] == target:
        return "YES"
    return "NO"


for i in to_find:
    print(bin_search(0, n - 1, list_num, i))