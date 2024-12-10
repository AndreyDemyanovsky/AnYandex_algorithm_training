n, k = map(int, input().split())
text = input()
left = right = 0

max_len = 0
fr_let = None
d = {}
while right < n:

    if text[right] not in d:
        d[text[right]] = 0

    if d[text[right]] + 1 <= k:

        d[text[right]] += 1
        if right - left + 1 > max_len:
            max_len = right - left + 1
            fr_let = left
        right += 1

    else:
        d[text[left]] -= 1
        left += 1

print(max_len, fr_let + 1)