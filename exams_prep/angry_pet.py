price_ratings = [int(i) for i in input().split()]
entry_point = int(input())
type_of_items = input()
type_of_price = input()
right_side = price_ratings.copy()
right_side = right_side[:entry_point]
left_side = price_ratings.copy()
left_side = left_side[entry_point+1:]
damage_right_side = 0
damage_left_side = 0
if type_of_items == 'cheap' and type_of_price == 'positive':
    damage_right_side = [i for i in right_side if price_ratings[entry_point] > i > 0]
    damage_left_side = [i for i in right_side if entry_point > i > 0]
elif type_of_items == 'cheap' and type_of_price == 'negative':
    damage_right_side = [i for i in right_side if entry_point > i < 0]
    damage_left_side = [i for i in right_side if entry_point > i < 0]
elif type_of_items == 'expensive' and type_of_price == 'positive':
    damage_right_side = [i for i in right_side if i >= entry_point and i > 0]
    damage_left_side = [i for i in right_side if entry_point and i > 0]
elif type_of_items == 'expensive' and type_of_price == 'negative':
    damage_right_side = [i for i in right_side if entry_point <= i < 0]
    damage_left_side = [i for i in right_side if entry_point <= i < 0]
if sum(damage_left_side) >= sum(damage_right_side):
    print(f'Left -> {sum(damage_left_side)}')
else:
    print(f'Right -> {sum(damage_right_side)}')



