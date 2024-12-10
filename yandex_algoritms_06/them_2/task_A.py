n = int(input())

list_number = list(map(int, input().split()))

prefixsum = [0]

for i in range(len(list_number)):
    new_prefixsum = list_number[i] + prefixsum[-1]
    prefixsum.append(new_prefixsum)

print(prefixsum)
     
