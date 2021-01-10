lines = int(input())
liters_poured = 0
for num in range(lines):
    quantity = int(input())
    if liters_poured + quantity > 255:
        print("Inceficiant capacity")
    elif liters_poured + quantity <= 255:
        liters_poured += quantity
print(liters_poured)