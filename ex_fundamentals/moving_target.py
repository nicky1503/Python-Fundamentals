targets = list(map(int, input().split(' ')))
while True:
    try:
        command, index, value = input().split()
    except ValueError:
        break
    index = int(index)
    value = int(value)
    if command == 'Shoot' and index< len(targets):
        targets[index] -= value
        targets = [nums for nums in targets if nums > 0]
    elif command == 'Add':
        if index < len(targets):
            targets.insert(index, value)
        else:
            print('Invalid placement!')
    elif command == 'Strike':
        if index - value >= 0 and index + value <= len(targets)-1:
            del targets[index-value:index+value+1]

        else:
            print('Strike missed!')
targets = list(map(str, targets))
result = ''.join([i + '|' for i in targets])
print(result[:-1])