import re
data = input()
list2 = []
while data:
    pattern = r"\d+"
    matches = re.findall(pattern, data)
    list2.append(matches)
    data = input()
list2 = [x for x in list2 if x]
list2 = [' '.join(i) for i in list2]
print(' '.join(list2))

