number_keys = int(input())
key_strength = list(map(int, input().split()))
dct = {}
number_clicks = int(input())

for index, strength in enumerate(key_strength):
    dct[index + 1] = [strength, "NO"]


for i in map(int, input().split()):
    strengthdct, info = dct[i]
    if info == "NO":
        if strengthdct - 1 == -1:
            dct[i][1] = "YES"
        dct[i][0] = strengthdct - 1
        
    
for i in dct:
    print(dct[i][1])
