sequenc = list(map(int, input().split()))
max1 = sequenc[0]
max2 = sequenc[1]
max3 = sequenc[2]
max3, max2, max1 = sorted(sequenc[:3])
min1, min2, min3 = max3, max2, max1

for i in range(3, len(sequenc)):
    element_seq = sequenc[i]

    if element_seq > max1:
        max3, max2, max1 = max2, max1, element_seq 
    elif element_seq > max2:
        max3, max2 = max2, element_seq
    elif element_seq > max3:
        max3 = element_seq
    
    if element_seq < min1:
        min3, min2, min1 = min2, min1, element_seq
    elif element_seq < min2:
        min3, min2 = min2, element_seq
    elif element_seq > min3:
        min3 = element_seq

multiplication_positive = max1 * max2 * max3
multiplication_negatives = min1 * min2 * min3
multiplication_mixed = min1 * min2 * max1
big_mul = max(multiplication_positive, multiplication_negatives, multiplication_mixed)

if big_mul == multiplication_positive:
    print(max1, max2, max3)
elif big_mul == multiplication_negatives:
    print(min1, min2, min3)
else:
    print(min1, min2, max1)

