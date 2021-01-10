neighbourhood = list(map(int, input().split('@')))
index_count = 0
successful_houses = []
data = input()
while data != 'Love!':
    jump, index = data.split()
    index = int(index)
    index_count += index
    if index_count < len(neighbourhood) and neighbourhood[index_count] != 'Done':
        neighbourhood[index_count] -= 2
    elif index_count >= len(neighbourhood):
        index_count = 0
        if neighbourhood[index_count] != 'Done':
            neighbourhood[0] -= 2
    if neighbourhood[index_count] == 0:
        print(f"Place {index_count} has Valentine's day.")
        neighbourhood[index_count] = 'Done'
    elif neighbourhood[index_count] == 'Done':
        print(f"Place {index_count} already had Valentine's day.")
    data = input()
successful_houses = [house for house in neighbourhood if house == 'Done']
print(f"Cupid's last position was {index_count}.")
if len(successful_houses) == len(neighbourhood):
    print('Mission was successful.')
else:
    print(f"Cupid has failed {len(neighbourhood) - len(successful_houses)} places.")
