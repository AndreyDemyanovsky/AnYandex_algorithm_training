t = int(input())

for _ in range(t):

    n = int(input())
    seq = list(map(int, input().split()))

    count_split = 0
    ls = []
    length_seq = 0
    min_in_seq = None

    for i in range(len(seq)):
        element = seq[i]
        if length_seq == 0:
            length_seq += 1
            min_in_seq = element
            count_split += 1
            if i == len(seq) - 1:
                ls.append(length_seq)
            continue

        if length_seq == min_in_seq or element < length_seq + 1:
            ls.append(length_seq)
            length_seq = 0
            min_in_seq = element
            count_split += 1
        length_seq += 1
        if i == len(seq) - 1:
            ls.append(length_seq)
        if element < min_in_seq:
            min_in_seq = element

    print(count_split)
    print(*ls)
