s = input()
q = int(input())
requests = tuple(tuple(map(int, input().split()))for i in range(q))

h = {}
power_x = {}
x = 257
h[0] = 0
power_x[0] = 1
p = 10**8 + 7
 
for i in range(1, len(s) + 1):
    res = (h[i - 1] * x + (ord(s[i - 1]) - 96)) % p
    h[i] = res
    power_x[i] = (power_x[i-1] * x) % p

def hash_substr(from_, lenght):
    # (h[from_ + lenght] + h[from2] * power_x[lenght]) при передаче третьего параметра который указывает на начальный индекс другого слова
    return (h[from_ + lenght] - h[from_] * power_x[lenght]) % p

 
for i in requests:
    lenght, first_ind, second_ind = i
    print("yes" if hash_substr(first_ind, lenght) == hash_substr(second_ind, lenght) else "no")
    