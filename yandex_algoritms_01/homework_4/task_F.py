import sys 

customers = {}

for line in sys.stdin:
    name, product, count = line.split()
    if name in customers:
        if product in customers[name]:
            customers[name][product] += int(count)
        else:
            customers[name][product] = int(count)   
    else:
        customers[name] = {product: int(count)}

        
for customer in sorted(customers):
    print(f"{customer}:")
    for product in sorted(customers[customer]):
        print(product, customers[customer][product])


