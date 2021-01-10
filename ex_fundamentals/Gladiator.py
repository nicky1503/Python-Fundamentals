lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price= float(input())
total_sum = 0
num_broke_shields = 0
for fight in range(1, lost_fights+1):
    if fight % 2 == 0:
        total_sum += helmet_price
    if fight % 3 == 0:
        total_sum += sword_price
        if fight % 2 == 0:
            total_sum += shield_price
            num_broke_shields += 1
    if num_broke_shields % 2 == 0 and num_broke_shields > 0:
        total_sum += armor_price
        num_broke_shields = 0
print(total_sum)

