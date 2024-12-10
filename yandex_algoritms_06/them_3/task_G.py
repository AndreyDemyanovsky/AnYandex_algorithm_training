
number_minuts, customers_per_minute = map(int, input().split())
customers = list(map(int, input().split()))
all_minut = 0
residue = 0

for number_customers in customers:
    all_customers = number_customers + residue
    all_minut += all_customers
    if all_customers - customers_per_minute > 0:
        residue = all_customers - customers_per_minute
    else:
        residue = 0
else:
    all_minut += residue

print(all_minut)
