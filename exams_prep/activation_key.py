def flip(kind_of_flip, start_index, end_index, result):
    result = [i for i in result]
    if kind_of_flip == "Lower":
        for index in range(len(result)):
            if start_index <= index < end_index:
                result[index] = result[index].lower()
    elif kind_of_flip == "Upper":
        for index in range(len(result)):
            if start_index <= index < end_index:
                result[index] = result[index].upper()
    result = ''.join(result)
    return result


def slice_key(start_index, end_index, result):
    result1 = [i for i in result]
    result = []
    for index in range(len(result1)):
        if not start_index <= index < end_index:
            result.append(result1[index])
    result = ''.join(result)
    return result


activation_key = input()
data = input()
while data != 'Generate':
    command = data.split('>>>')
    task = command[0]
    if task == 'Contains':
        if command[1] in activation_key:
            print(f"{activation_key} contains {command[1]}")
        else:
            print("Substring not found!")
    elif task == 'Flip':
        activation_key = flip(command[1], int(command[2]), int(command[3]), activation_key)
        print(activation_key)
    elif task == 'Slice':
        activation_key = slice_key(int(command[1]), int(command[2]), activation_key)
        print(activation_key)
    data = input()
print(f'Your activation key is: {activation_key}')