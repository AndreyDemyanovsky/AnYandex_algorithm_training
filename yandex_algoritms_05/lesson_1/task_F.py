n = int(input())
nums = list(map(int, input().split()))

operation = ""
is_not_even1 = True if nums[0] % 2 == 1 else False

for i in range(1, n):
    is_not_even2 = True if nums[i] % 2 == 1 else False
    if is_not_even2 and is_not_even1:
        operation += "x"
    else:
        operation += "+"
        if (is_not_even1 and not is_not_even2) or (not is_not_even1 and is_not_even2):
            is_not_even1 = True
        else:
            is_not_even1 = False

print(operation)
