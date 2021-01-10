data = input()
products = {}
while data != 'buy':
    key, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    if key not in products:
        products[key] = []
        products[key].append(price*quantity)
        products[key].append(quantity)
    else:
        products[key][0] = (products[key][1]+quantity)*price
        products[key][1] += quantity
    data = input()
for k, v in products.items():
    print(f"{k} -> {v[0]:.2f}")