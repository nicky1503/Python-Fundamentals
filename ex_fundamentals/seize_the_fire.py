fire_sells = list(input().split('#'))
given_water = int(input())
sell_level = []
fire_put_out = 0
print("Cells:")
for num in range(len(fire_sells)):
    sell_level.append(fire_sells[num].split(' = '))
for index in range(len(sell_level)):
    if sell_level[index][0] == 'High' and 81 <= int(sell_level[index][1]) <= 125:
        if given_water >= int(sell_level[index][1]):
            given_water -= int(sell_level[index][1])
            fire_put_out += int(sell_level[index][1])
            print(f" - {int(sell_level[index][1])}")
    elif sell_level[index][0] == 'Medium' and 51 <= int(sell_level[index][1]) <= 80:
        if given_water >= int(sell_level[index][1]):
            given_water -= int(sell_level[index][1])
            fire_put_out += int(sell_level[index][1])
            print(f" - {int(sell_level[index][1])}")
    elif sell_level[index][0] == 'Low' and 1 <= int(sell_level[index][1]) <= 50:
        if given_water >= int(sell_level[index][1]):
            given_water -= int(sell_level[index][1])
            fire_put_out += int(sell_level[index][1])
            print(f" - {int(sell_level[index][1])}")
print(f"Effort: {fire_put_out*0.25:.2f}")
print(f'Total Fire: {fire_put_out}')






















#High = 89#Low = 28#Medium = 77#Low = 23