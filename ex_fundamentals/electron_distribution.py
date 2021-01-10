number_of_electrons = int(input())
shield_number = 1
result = []
while True:
    number_electrons_for_shield = 2*shield_number**2
    shield_number += 1
    if number_of_electrons >= number_electrons_for_shield:
        result.append(number_electrons_for_shield)
        number_of_electrons -= number_electrons_for_shield
    else:
        break
result.append(number_of_electrons)
print(result)


