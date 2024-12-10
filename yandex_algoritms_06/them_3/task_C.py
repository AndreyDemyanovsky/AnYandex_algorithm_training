length_seq, size_window = map(int, input().split())
list_numbers = list(map(int, input().split()))
dec = []

start_print = False
for i in range(length_seq):

    if i + 1 == size_window:
        start_print = True

    while dec and list_numbers[i] < dec[-1]:
        del dec[-1]
    dec.append(list_numbers[i])

    if start_print:
        print(dec[0])
        if list_numbers[i + 1 - size_window] == dec[0]:
            del dec[0]

