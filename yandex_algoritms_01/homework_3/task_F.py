genom1 = input()
genom2 = input()

dct = {}
set_genum2 = set()


for i in range(len(genom2) - 1):
    set_genum2.add(genom2[i:i+2])

for i in range(len(genom1) - 1):
    sub_str = genom1[i:i + 2]
    if sub_str not in dct:
        dct[sub_str] = 1
    else:
        dct[sub_str] += 1


count = 0
for i in set_genum2:
    if i in dct:
        count += dct[i]

print(count)