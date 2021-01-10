#numbers_as_string = input().split(', ')
#even_numbers = [numbers_as_string.index(num) for num in numbers_as_string if int(num) % 2 == 0]
#print(even_numbers)

nums_as_string = list(map(int, input().split()))
convert_to_string = list(map(lambda num: str(num), nums_as_string))
print(nums_as_string)
print(convert_to_string)
