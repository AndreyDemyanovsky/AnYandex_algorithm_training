n_color_tshirt = int(input())
tshirt = list(map(int, input().split()))

n_color_trousers = int(input())
trousers = list(map(int, input().split()))

p1 = 0
p2 = 0
res = float("inf")
num1 = num2 = 0

while p1 <= n_color_tshirt - 1 and p2 <= n_color_trousers - 1:
    if abs(tshirt[p1] - trousers[p2]) < res:
        res = abs(tshirt[p1] - trousers[p2])
        num1 = tshirt[p1]
        num2 = trousers[p2]
    if tshirt[p1] > trousers[p2]:
        p2 += 1
    else:
        p1 += 1

print(num1, num2)
