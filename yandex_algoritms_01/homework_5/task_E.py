n_trees, number_types = map(int, input().split())
trees = list(map(int, input().split()))
left_p = right_p = 0
window = {i: 0 for i in range(1, number_types + 1)}

settree = set()
min_len = float("inf")
l = r = None
while right_p <= n_trees:
    if window[trees[left_p]] > 1:
        window[trees[left_p]] -= 1
        left_p += 1
    else:
        if right_p < n_trees:
            window[trees[right_p]] += 1
            settree.add(trees[right_p])
        right_p += 1

    if len(settree) == number_types and right_p - left_p < min_len:
        min_len = right_p - left_p
        l = left_p
        r = right_p


print(l + 1, r)