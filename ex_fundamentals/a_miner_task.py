material = input()

result = {}
while material != 'stop':
    quantity = int(input())
    if material not in result:
        result[material] = quantity
    else:
        result[material] += quantity
    material = input()

for k, v in result.items():
    print(f"{k} -> {v}")