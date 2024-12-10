n, k = map(int, input().split())

cars = list(map(int, input().split()))

l = r = 0

result = 0
summa = 0

while l <= n - 1 and r <= n:

    if summa > k:
        summa -= cars[l]
        l += 1
    else:
        if summa == k:
            result += 1
            summa -= cars[l]
            l += 1
        if r <= n - 1:
            summa += cars[r]
        r += 1

print(result)
