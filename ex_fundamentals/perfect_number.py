def perfect_number(number):
    result = 0
    for divider in range(1, number):
        if number % divider == 0:
            result += divider
    if result == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)

