n, m = map(int, input().split())

events = []

for _ in range(m):
    n_st, n_end = map(int, input().split())
    events.append((n_st, n_end))
events.sort()

count_people = 0
start = end = None


for i in events:
    st, en = i
    if start is None or end is None:
        start = st
        end = en

    if start <= st <= end:
        if end < en:
            end = en
    else:
        count_people += end - start + 1
        start = st
        end = en
else:
    count_people += end - start + 1

print(n - count_people)
