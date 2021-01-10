def urgent(product):
    if product not in shopping_list:
        shopping_list.insert(0, product)
    return shopping_list


def unnecessary(product):
    if product in shopping_list:
        shopping_list.remove(product)
    return shopping_list


def correct(old_item, new_item):
    if old_item in shopping_list:
        shopping_list[shopping_list.index(old_item)] = new_item
    return shopping_list


def rearrange(prduct):
    if prduct in shopping_list:
        res = shopping_list.pop(shopping_list.index(prduct))
        shopping_list.append(res)
    return shopping_list


shopping_list = input().split('!')
products_to_add = input()
while products_to_add != 'Go Shopping!':
    command = products_to_add.split()
    if command[0] == 'Urgent':
        (urgent(command[1]))
    elif command[0] == 'Unnecessary':
        (unnecessary(command[1]))
    elif command[0] == 'Correct':
        correct(command[1], command[2])
    elif command[0] == 'Rearrange':
        rearrange(command[1])
    products_to_add = input()
print(', '.join(shopping_list))