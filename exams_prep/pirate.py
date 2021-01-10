data = input()
cities = {}
while data != 'Sail':
    data = data.split('||')
    if data[0] not in cities:
        cities[data[0]] = (data[1:])
    else:
        cities[data[0]][0] = int(cities[data[0]][0]) + int(data[1])
        cities[data[0]][1] = int(cities[data[0]][1]) + int(data[2])
    cities[data[0]][0] = int(cities[data[0]][0])
    cities[data[0]][1] = int(cities[data[0]][1])
    data = input()

data2 = input()
while data2 != 'End':
    data2 = data2.split('=>')
    city = data2[1]
    if data2[0] == 'Plunder':
        population = int(data2[2])
        gold = int(data2[3])

        if int(cities[city][0]) > 0 and int(cities[city][1]) > 0:
            cities[city][0] = int(cities[city][0]) - int(population)
            cities[city][1] = int(cities[city][1]) - int(gold)
            print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
        if int(cities[city][0]) == 0 or int(cities[city][1]) == 0:
            print(f"{city} has been wiped off the map!")
            cities.pop(city)
    elif data2[0] == 'Prosper':
        gold = int(data2[2])
        if int(gold) < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[city][1] = int(cities[city][1]) + int(gold)
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city][1]} gold.")
    data2 = input()
if len(cities) > 0:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    sorted_key_items = sorted(cities.items(), key=lambda x: (-x[1][1], x[0]))
    for key, value in sorted_key_items:
        print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
