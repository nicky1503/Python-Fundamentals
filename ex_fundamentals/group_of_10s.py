numbers = list(map(int, input().split(', ')))
sorted(numbers)
tens = 10
lenght_of_result = 0
while True:
    result = [num for num in numbers if tens >= num >= tens - 10]
    print(f"Groups of {tens}'s: {result}")
    lenght_of_result += len(result)
    tens += 10
    result.clear()
    if len(numbers) == lenght_of_result:
        break
