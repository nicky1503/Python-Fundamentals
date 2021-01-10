def subtract_function(a, b, c):
    def sum_numbers():
        sum_of_ints = a + b
        return sum_of_ints

    def subtract_nums():
        return sum_numbers() - c
    return subtract_nums()


a = int(input())
b = int(input())
c = int(input())
print(subtract_function(a, b, c))