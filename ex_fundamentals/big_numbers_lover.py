def find_num_lenght(all_numbers):
    pass


numbers = input().split()
numbers = sorted(numbers, reverse=True)
result = ''.join([num for num in numbers])
print(result)
