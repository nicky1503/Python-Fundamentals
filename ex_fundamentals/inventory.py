def does_item_exist(items, item):
    for i in items:
        if i == item:
            return True
    return False


def collect_item(items, item):
    if does_item_exist(items, item):
        return items
    else:
        items.append(item)
        return items


def drop_item(items, item):
    if does_item_exist(items, item):
        items.remove(item)
    return items


def combine_items(items, item):
    old_item, new_item = item.split(':')
    if does_item_exist(items, old_item):
        items.insert(items.index(old_item) + 1, new_item)
    return items


def renew_items(items, item):
    if does_item_exist(items, item):
        item_to_be_renewed = item
        items.remove(item)
        items.append(item_to_be_renewed)
    return items


items = input().split(', ')
commands = input()
while commands != 'Craft!':
    command, item = commands.split(' - ')
    if command == 'Collect':
        collect_item(items, item)
    elif command == 'Drop':
        drop_item(items, item)
    elif command == 'Renew':
        renew_items(items, item)
    elif command == "Combine Items":
        combine_items(items, item)
    commands = input()
print(', '.join(items))
