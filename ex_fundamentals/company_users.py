data = input()
users = {}
while data != 'End':
    company, id_num = data.split(' -> ')
    if company not in users:
        users[company] = []
        users[company].append(id_num)
    else:
        if id_num not in users[company]:
            users[company].append(id_num)
    data = input()

sorted_users = dict(sorted(users.items(), key=lambda x: x[0]))
for key, value in sorted_users.items():
    print(f"{key}")
    for i in range(len(value)):
        print(f"-- {value[i]}")
