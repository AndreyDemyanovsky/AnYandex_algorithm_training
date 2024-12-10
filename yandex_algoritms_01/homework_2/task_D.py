list_numbers = list(map(int, input().split()))

counter = 0

for i in range(1, len(list_numbers) - 1):
    element = list_numbers[i]
    if list_numbers[i - 1] < element and list_numbers[i + 1] < element:
        counter += 1

print(counter)