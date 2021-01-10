def print_legendary_item(key):
    if key == 'shards':
        return print("Shadowmourne obtained!")
    elif key == 'fragments':
        return print("Valanyr obtained!")
    elif key == 'motes':
        return print("Dragonwrath obtained!")


data = input()
other_items = {}
key_items = {'shards': 0, 'fragments': 0, "motes": 0}
find_legendary_item = False
while True:
    data = data.lower().split()
    for i in range(0, len(data), 2):
        key = data[i + 1]
        value = int(data[i])
        if key == 'shards' or key == 'fragments' or key == 'motes':
            key_items[key] += value
        elif key != 'shards' and key != 'fragments' and key != 'motes':
            if key not in other_items:
                other_items[key] = value
            else:
                other_items[key] += value
        for key, num in key_items.items():
            if num >= 250:
                find_legendary_item = True
                print_legendary_item(key)
                key_items[key] -= 250
                break
        if find_legendary_item:
            break
    if find_legendary_item:
        break
    data = input()
if len(key_items) >= 3:
    sorted_key_items = dict(sorted(key_items.items(), key=lambda x: (-x[1], x[0])))
else:
    sorted_key_items = dict(sorted(key_items.items(), key=lambda x: -x[1]))
for k, v in sorted_key_items.items():
    print(f"{k}: {v}")
sorted_junk = dict(sorted(other_items.items(), key=lambda x: x[0]))

for kj, vj in sorted_junk.items():
    print(f"{kj}: {vj}")



