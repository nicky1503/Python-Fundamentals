def add_people_to_train(people):
    train_bussiness[len(train_bussiness)-1] += people
    return train_bussiness


def insert_people_at_given_index(people, index):
    train_bussiness[index] += people
    return train_bussiness


def remove_people_at_given_index(people, index):
    train_bussiness[index] -= people
    return train_bussiness


wagens = int(input())
train_bussiness = [num * 0 for num in range(wagens)]
user_input = input().split()
while user_input[0] != 'End':
    if user_input[0] == 'add':
        add_people_to_train(int(user_input[1]))
    elif user_input[0] == 'insert':
        insert_people_at_given_index(int(user_input[2]), int(user_input[1]))
    elif user_input[0] == 'leave':
        remove_people_at_given_index(int(user_input[2]), int(user_input[1]))
    user_input = input().split()
print(train_bussiness)
