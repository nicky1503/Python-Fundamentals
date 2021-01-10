donations = list(input().split(', '))
number_of_beggars = int(input())
result = []
counter = 0
sum_for_beggar = 0
for _ in range(number_of_beggars):
    for index in range(counter, len(donations), number_of_beggars):
        sum_for_beggar += int(donations[index])
    counter += 1
    result.append(sum_for_beggar)
    sum_for_beggar = 0
print(result)

