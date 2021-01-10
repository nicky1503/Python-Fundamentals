numbers = list((input()).split())
numbers_to_be_removed = int(input())
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for index in range(numbers_to_be_removed):
    numbers.remove(min(numbers))
print(numbers)
