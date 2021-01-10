item = input()
num = int(input())


def total(quantity, product):
    result = 0
    if product == "coffee":
        result = quantity*1.5
    elif product == "water":
        result = quantity*1
    elif product == "coke":
        result = quantity*1.4
    elif product == "snacks":
        result = quantity*2
    return result


print(round(total(num, item), 2))

