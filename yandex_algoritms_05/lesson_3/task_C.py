n = int(input())

dct = {}
lst = list(map(int, input().split()))

for i in lst:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1

max_last_of_number = None
for i in dct:
    last_of_number = dct[i]

    plus_one = dct[i + 1] if i + 1 in dct else None
    minus_one = dct[i - 1] if i - 1 in dct else None

    if plus_one:
        if minus_one:
            last_of_number += plus_one if plus_one > minus_one else minus_one
        else:
            last_of_number += plus_one
    elif minus_one:
        last_of_number += minus_one

    if not max_last_of_number:
        max_last_of_number = last_of_number
    else:
        if last_of_number > max_last_of_number:
            max_last_of_number = last_of_number

print(n - max_last_of_number)