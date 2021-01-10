emp_1 = int(input())
emp_two = int(input())
emp_3 = int(input())
num_people = int(input())
h_needed = 0
answers_per_h = emp_1 + emp_3 + emp_two
people_answered = 0
h_worked = 0
while people_answered < num_people:
    h_needed += 1
    h_worked += 1
    people_answered += answers_per_h
    if h_worked == 3 and people_answered<num_people:
        h_worked = 0
        h_needed += 1

print(f"Time needed: {h_needed}h.")