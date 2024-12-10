list_numbers = list(map(int, input().split()))
flag = "YES"
save_element = list_numbers[0]

for i in range(1, len(list_numbers)):
    if list_numbers[i] <= save_element:
        flag = "NO"
        break
    save_element = list_numbers[i]

print(flag)