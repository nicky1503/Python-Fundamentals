import re
data = input()
#pattern = r"(^|(?<=\s))[a-z0-9][a-z0-9\._-]+-?@[a-z0-9-]+\.[a-z\.?]+[a-z](?=[\s,.])"
pattern = r"(^|(?<=\s))[a-z0-9][a-z0-9\._-]+-?@[a-z0-9-]+\.[a-z\.?]+[a-z0-9]\b"
matches = re.finditer(pattern, data)
for var in matches:
    print(var.group())