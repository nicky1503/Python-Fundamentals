import sys


def smallest_number():
    smallest = sys.maxsize
    for num in range(3):
        integer = int(input())
        if integer < smallest:
            smallest = integer
    return smallest


print(smallest_number())
