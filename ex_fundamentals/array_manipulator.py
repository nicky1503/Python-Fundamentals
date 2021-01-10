def exchange_string(user_input, value):
    if len(user_input) > value:
        second_half = user_input[value + 1:]
        first_half = user_input[:value+1]
        result = second_half + first_half
        return result
    else:
        print('Invalid index')


def max_even_or_odd(user_input, value):
    if value == 'even':
        try:
            sorted_even = max(list(filter(lambda x: (x % 2 == 0), user_input)))
            return user_input.index(sorted_even)
        except ValueError:
            return 'No matches'

    elif value == 'odd':
        try:
            sorted_odd = max(list(filter(lambda x: (x % 2 == 1), user_input)))
            return user_input.index(sorted_odd)
        except ValueError:
            return 'No matches'


def min_even_or_odd(user_input, value):
    if value == 'even':
        try:
            sorted_even = min(list(filter(lambda x: (x % 2 == 0), user_input)))
            return user_input.index(sorted_even)
        except ValueError:
            return 'No matches'

    elif value == 'odd':
        try:
            sorted_odd = min(list(filter(lambda x: (x % 2 == 1), user_input)))
            return user_input.index(sorted_odd)
        except ValueError:
            return 'No matches'


def count_first_even_or_odd(user_input, value, count):
    count = int(count)
    if value == 'even':
        if not (count > len(user_input)):
            sorted_even = (list(filter(lambda x: (x % 2 == 0), user_input)))
            sorted_even.sort()
            return sorted_even[:count]
        else:
            return 'Invalid count'
    elif value == 'odd':
        if not (count > len(user_input)):
            sorted_odd = (list(filter(lambda x: (x % 2 == 1), user_input)))
            sorted_odd.sort()
            return sorted_odd[:count]
        else:
            return 'Invalid count'


def count_last_even_or_odd(user_input, value, count):
    count = int(count)
    if value == 'even':
        if not (count > len(user_input)):
            sorted_even = (list(filter(lambda x: (x % 2 == 0), user_input)))
            sorted_even.sort(reverse=True)
            sorted_nums = sorted_even[:count]
            sorted_nums.sort()
            return sorted_nums
        else:
            return 'Invalid count'
    elif value == 'odd':
        if not (count > len(user_input)):
            sorted_odd = (list(filter(lambda x: (x % 2 == 1), user_input)))
            sorted_odd.sort(reverse=True)
            sorted_nums = sorted_odd[:count]
            sorted_nums.sort()
            return sorted_nums
        else:
            return 'Invalid count'


user_input = list(map(int, input().split()))
command = input().split()
while command[0] != 'end':
    if command[0] == 'exchange':
        exchange_string(user_input, int(command[1]))
    elif command[0] == 'max':
        print(max_even_or_odd(user_input, command[1]))
    elif command[0] == 'min':
        print(min_even_or_odd(user_input, command[1]))
    elif command[0] == 'first':
        print(count_first_even_or_odd(user_input, command[2], command[1]))
    elif command[0] == 'last':
        print(count_last_even_or_odd(user_input, command[2], command[1]))
    command = input().split()
if command[0] == 'end':
    print(user_input)