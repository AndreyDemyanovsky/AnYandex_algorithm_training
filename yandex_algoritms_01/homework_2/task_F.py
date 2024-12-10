N = int(input())
sequenc = list(map(int, input().split()))

len_prefix = 0
faind = True
i = 0

while faind:
    left_part = sequenc[i:]
    right_part = sequenc[-1: -len(sequenc) + (i - 1): -1]
    
    if left_part == right_part:
        len_prefix = i
        faind = False
    i += 1


print(len_prefix)
if len_prefix:
    prefix = sequenc[:len_prefix]
    print(*prefix[::-1])
