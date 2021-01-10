people_to_get_on_lift = int(input())
lift_cabins = [int(x) for x in input().split()]
for i in range(len(lift_cabins)):
    while lift_cabins[i] < 4 and people_to_get_on_lift > 0:
        lift_cabins[i] += 1
        people_to_get_on_lift -= 1
if people_to_get_on_lift == 0 and sum(lift_cabins) == len(lift_cabins*4):
    print(' '.join([str(x) for x in lift_cabins]))
elif people_to_get_on_lift == 0 and sum(lift_cabins) < len(lift_cabins*4):
    print("The lift has empty spots!")
    print(' '.join([str(x) for x in lift_cabins]))
else:
    print(f"There isn't enough space! {people_to_get_on_lift} people in a queue!")
    print(' '.join([str(x) for x in lift_cabins]))
