def palindrome_finder(numbers):
    number = numbers.split(', ')
    for index in range(len(number)):
        indexes_of_num = str(number[index])
        if indexes_of_num[0] == indexes_of_num[len(indexes_of_num)-1]:
            print('True')
        else:
            print('False')


numbers = input()
palindrome_finder(numbers)
