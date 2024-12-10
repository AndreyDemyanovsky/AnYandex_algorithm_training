N, K = map(int, input().split())

list_number = list(map(int, input().split()))

l = 0
r = 0
result = 0
summa = list_number[0]

while l < len(list_number) and r < len(list_number):

    if summa == K:
        result += 1
        summa -= list_number[l]
        l += 1
        r += 1
        if r < len(list_number):
            summa += list_number[r]
    elif summa < K:
        r += 1
        if r < len(list_number):
            summa += list_number[r]
    elif summa > K:
        summa -= list_number[l]
        l += 1

print(result)
