people = int(input())
max_capacity = int(input())
people_transported = 0
courses= 0
people_left = 0
while True:
    if people - people_transported <= 0:
        break
    people_transported += max_capacity
    courses += 1

print(courses)
