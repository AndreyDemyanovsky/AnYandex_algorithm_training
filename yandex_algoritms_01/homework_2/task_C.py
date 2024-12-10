
N = int(input())
list_number = list(map(int, input().split()))
x = int(input())
closest = 10000
difference_closese = 20001

for i in list_number:
    df = x - i
    if x < i:
        df *= (-1)
    if df < difference_closese:
        closest = i
        difference_closese = df

print(closest)
