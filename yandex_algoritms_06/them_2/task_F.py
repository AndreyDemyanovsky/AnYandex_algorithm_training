n = int(input())
list_number = list(map(int, input().split()))
prefix_sum = list_number[0]
sufix_sum = 0

for i in range(2, n):
    sufix_sum += list_number[i]

result = 0
for i in range(1, n - 1):
    result += (list_number[i] * prefix_sum * sufix_sum) % 1000000007
    prefix_sum += list_number[i]
    sufix_sum -= list_number[i + 1]

print(result % 1000000007)
