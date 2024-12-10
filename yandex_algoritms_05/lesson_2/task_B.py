days, k = map(int, input().split())
prices = list(map(int, input().split()))

purchase_price = 0
purchase_day = 0
dif = 0
for ind, price in enumerate(prices):
    if purchase_price == 0 or price <= purchase_price:
        purchase_price = price
        purchase_day = ind
    if price - purchase_price >= dif:
        dif = price - purchase_price
    if ind - purchase_day == k:
        purchase_price = price
        purchase_day = ind


print(dif)