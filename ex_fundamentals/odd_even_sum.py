def odd_and_even_sum(numbers):
    even_numbers = 0
    odd_numbers = 0
    for num in numbers:
        num = int(num)
        if num % 2 == 0 and num != 0:
            even_numbers += num
        else:
            odd_numbers += num
    return even_numbers, odd_numbers


numbers = input()
print(f'Odd sum = {odd_and_even_sum(numbers)[1]}, Even sum = {odd_and_even_sum(numbers)[0]}')