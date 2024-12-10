count_sect = int(input())
sectors = list(map(int, input().split()))
visit = [0] * count_sect
min_v, max_v, k = map(int, input().split())

m = 0
for v in range(min_v, max_v + 1, k):
    if sum(visit) == count_sect:
        break
    right_sec = v // k
    if v % k == 0:
        right_sec -= 1
    if right_sec > count_sect - 1:
        right_sec = right_sec % count_sect
    left_sec = right_sec * (-1)
    if sectors[right_sec] > m:
        m = sectors[right_sec]
    visit[right_sec] = 1
    if sectors[left_sec] > m:
        m = sectors[left_sec]
    visit[left_sec] = 1

print(m)
