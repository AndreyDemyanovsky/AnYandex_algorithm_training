size = length_sequence = int(input())
sequence = list(map(int, input().split()))
sequence.sort()
result = []

number_delete_median = 0

while size != 0:
    if size % 2 != 0:
        l = r = size // 2
        result.append(sequence[r + number_delete_median])
        number_delete_median += 1
        size -= 1
    else:
        r = size // 2
        l = r - 1
        result.append(sequence[l])
        number_delete_median += 1
        size -= 1

print(*result)







