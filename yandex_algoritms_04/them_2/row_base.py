def get_hash(s):
    
    x = 10
    h = {}
    h[0] = 0
    power_x = {}
    power_x[0] = 1
    p = 10**8 + 7
    
    for i in range(1, len(s) + 1):
        res = (h[i - 1] * x + (ord(s[i - 1]) - 96)) % p
        h[i] = res
        power_x[i] = (power_x[i-1] * x) % p
    return h, power_x


s = input()
h, power_x = get_hash(s)
k = 1
while h[len(s) - k] != (h[len(s)] - h[k] * power_x[len(s) - k]) % (10**8 + 7):
    k += 1
print(k)

