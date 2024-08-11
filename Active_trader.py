def mostActive(customers):
    d = {}
    for c in customers:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
            
    minimum = 0.05 * len(customers)
    active = []
    for c, cnt in d.items():
        if cnt >= minimum:
            active.append(c)
    active.sort()
    
    return active


customers_count = int(input())

customers = []

for i in range(customers_count):
    customers_item = input()
    customers.append(customers_item)

result = mostActive(customers)

print('\n'.join(result))