number_evidence = int(input())
amount_evidence = list(map(int, input().split()))
number_experiments, number_movements = map(int, input().split())
start_evidence = list(map(int, input().split()))

list_minimal_left = [0]
for i in range(1, len(amount_evidence)):
    if amount_evidence[i] >= amount_evidence[i - 1]:
        list_minimal_left.append(list_minimal_left[-1])
    else:
        list_minimal_left.append(i)


list_minimal_number_movements = []
l = len(amount_evidence) - 1
r = len(amount_evidence) - 1
k = 0
while r != 0 or l != 0:
    r -= 1
    if amount_evidence[r] == amount_evidence[r + 1]:
        k += 1

    while k > number_movements:
        list_minimal_number_movements.append(r + 1)
        if amount_evidence[l - 1] == amount_evidence[l]:
            k -= 1
        l -= 1

    if r == 0:
        list_minimal_number_movements.extend([0] * (l - r + 1))
        l = 0
if not list_minimal_number_movements:
    list_minimal_number_movements.append(0)
list_minimal_number_movements.reverse()

result = []
for i in start_evidence:
    ind = i - 1
    if  list_minimal_number_movements[ind] > list_minimal_left[ind]:
        result.append(list_minimal_number_movements[ind] + 1)
    else:
        result.append(list_minimal_left[ind] + 1)

print(*result)
