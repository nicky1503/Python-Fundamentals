data = input().split()
products_to_check = input().split()
items = {}
for i in range(0, len(data), 2):
    key = data[i]
    value = data[i+1]
    items[key] = value


for item in products_to_check:
    if item in items:
        print(f"We have {items.get(item)} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
