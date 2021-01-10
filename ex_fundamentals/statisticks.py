products = input()
storage = {}
quantity = 0
while products != 'statistics':
    key, value = products.split(": ")
    value = int(value)
    quantity += value
    if key not in storage:
        storage[key] = value

    else:
        storage[key] += value
    products = input()
for k, v in storage.items():
    print(f"{k}: {v}")
print(f"Total Products: {len(storage)}")
print(f"Total Quantity: {quantity}")