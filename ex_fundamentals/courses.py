data = input()
courses = {}
while data != 'end':
    course, name = data.split(' : ')
    if course not in courses:
        courses[course] = []
        courses[course].append(name)
    else:
        courses[course].append(name)
    data = input()

sorted_students = dict(sorted(courses.items(), key=lambda x: -len(x[1])))
# for k, v in sorted_students.items():
#     sorted_students[k] = sorted_students[v].sort()
for x in sorted_students:
    sorted_students[x].sort()
for key, value in sorted_students.items():
    print(f"{key}: {len(value)}")
    for i in range(len(value)):
        print(f"-- {value[i]}")