nums = int(input())
students = {}
for _ in range(nums):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
        students[name].append(grade)
    else:
        students[name].append(grade)

for name, grades in list(students.items()):
    if sum(grades)/len(grades) < 4.5:
        students.pop(name)
    else:
        students[name] = sum(grades)/len(grades)
sorted_students = dict(sorted(students.items(), key=lambda x: -x[1]))
for k, v in sorted_students.items():
    print(f"{k} -> {v:.2f}")
