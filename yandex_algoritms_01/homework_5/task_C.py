n = int(input())

y_on_route = [0]
up = [0]
revers_up = [0]

for _ in range(n):
    x, y = map(int, input().split())

    if y > y_on_route[-1]:
        up.append(y - y_on_route[-1] + up[-1])
        revers_up.append(revers_up[-1])
    else:
        up.append(up[-1])
        revers_up.append(y_on_route[-1] - y + revers_up[-1])

    y_on_route.append(y)

k = int(input())
for _ in range(k):
    start, end = map(int, input().split())
    if start <= end:
        print(up[end] - up[start])
    else:
        print(revers_up[start] - revers_up[end])