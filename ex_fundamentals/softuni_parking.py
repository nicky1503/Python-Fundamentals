def register_car(name, number):
    if name not in cars:
        cars[name] = number
        return f"{name} registered {number} successfully"
    else:
        return f"ERROR: already registered with plate number {number}"


def unregister_car(name):
    if name not in cars:
        return f"ERROR: user {name} not found"
    else:
        cars.pop(name)
        return f"{name} unregistered successfully"


times = int(input())
cars = {}
for i in range(times):
    commands = input().split()
    command = commands[0]
    if command == 'register':
        print(register_car(commands[1], commands[2]))
    elif command == 'unregister':
        print(unregister_car(commands[1]))
for k, v in cars.items():
    print(f"{k} => {v}")