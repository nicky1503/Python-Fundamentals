notes = input()
importance = []
while notes != 'End':
    importance.append(notes)
    notes = input()

importance.sort()
importance = [task[2:] for task in importance]
print(importance)