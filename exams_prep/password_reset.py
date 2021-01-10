password = input()
data = input()
result = None
while data != "Done":
    data = data.split()
    task = data[0]
    if task == 'TakeOdd':
        result = [password[char] for char in range(1, len(password), 2)]
        password = "".join(result)
        print(password)
    elif task == 'Cut':
        start_index = int(data[1])
        end_index = int(data[2])+start_index-1
        result = [password[index] for index in range(len(password)) if index < start_index or index > end_index]
        password = ''.join(result)
        print(password)
    elif task == 'Substitute':
        substring = data[1]
        substitute = data[2]
        if substring in password:
            while substring in password:
                password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    data = input()
print(f'Your password is: {password}')