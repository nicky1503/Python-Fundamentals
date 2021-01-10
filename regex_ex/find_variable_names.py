import re
data = input()
pattern = r"(^_|(?<=\s_))[a-z,A-Z]+($|(?=\s))"
matches = re.finditer(pattern, data)
result = []
for var in matches:
    result.append(var.group())
print(','.join(result))