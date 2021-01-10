import re
numbers = input()
pattern = r"(^|(?<=\s))-*\d+\.*\d*($|(?=\s))"
matches = re.finditer(pattern, numbers)
for num in matches:
    print(num.group(), end=' ')