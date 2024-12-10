n, k = map(int, input().split())
numbers = list(map(int, input().split()))

dct_ind = {}
ans = "NO"
for ind, value in enumerate(numbers):
    if value not in dct_ind:
        dct_ind[value] = ind
    else:
        if ind - dct_ind[value] <= k:
            ans = "YES"
            break
        dct_ind[value] = ind

print(ans)
