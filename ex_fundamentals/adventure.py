import math
party_size = int(input())
num_of_days = int(input())
coins = 0
coins_per_person = 0
for day in range(1, num_of_days+1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    if day % 3 == 0:
        coins -= party_size*3
    if day % 5 == 0:
        coins += party_size*20
        if day % 3 == 0:
            coins -= party_size*2
    coins += 50
    coins -= party_size * 2
coins_per_person = coins/party_size
print(math.floor(coins_per_person))

