number_citys = int(input())
avg_price_live = enumerate(map(int, input().split()))
stack = []
result = [-1] * number_citys

for i in avg_price_live:
    if not stack:
        stack.append(i)
    else:
        while stack and i[1] < stack[-1][1]:
            ind, value = stack.pop()
            result[ind] = i[0]
        stack.append(i)
print(*result)
