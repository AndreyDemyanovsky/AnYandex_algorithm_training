profit, number_founders, days = map(int, input().split())
save = profit

for i in range(0, 10):
    if ((profit * 10) + i) % number_founders == 0:
        profit = (profit * 10) + i
        days -= 1
        break

print(str(profit) + "0" * days if save != profit else -1)
