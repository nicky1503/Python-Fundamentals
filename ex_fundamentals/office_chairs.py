number_of_rooms = int(input())
free_chairs = 0
message = []
enough_chairs = True
for room in range(1, number_of_rooms + 1):
    available_chairs, needed_chairs = input().split()
    int(needed_chairs)
    if len(available_chairs) >= int(needed_chairs):
        free_chairs += len(available_chairs) - int(needed_chairs)
    else:
        message.append(f'{int(needed_chairs) - len(available_chairs)} more chairs needed in room {room}')
        enough_chairs = False
if enough_chairs:
    print(f'Game On, {free_chairs} free chairs left')
else:
    message = [print(m) for m in message]


