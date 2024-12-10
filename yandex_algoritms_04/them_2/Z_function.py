import sys

def hash_s(s):
    h = [0]
    power_x = [1]
    x = 257
    p = 10 ** 8 + 7

    for i in range(1, len(s) + 1):
        res = (h[i - 1] * x + (ord(s[i - 1]) - 96)) % p
        h.append(res)
        power_x.append((power_x[i - 1] * x) % p)
    return h, power_x


def z_function(row):
    h, power_x = hash_s(row)
    arr_z_function = [0]

    for i in range(1, len(row)):
        z = 0
        right = len(row)
        left = i

        while left <= right:
            middle = (left + right) // 2

            if (h[middle] - h[i] * power_x[middle - i]) % (10 ** 8 + 7) == h[middle - i]:
                z = middle - i
                left = middle + 1
            else:
                right = middle - 1
        arr_z_function += [z]

    return arr_z_function


print(*z_function(sys.stdin.readline().strip()))   
            

            




