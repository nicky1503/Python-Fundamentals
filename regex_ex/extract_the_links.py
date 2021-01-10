import re
data = input()
pattern = r"www\.[A-Za-z0-9-]+\.[a-z][a-zA-z0-9\.-]+\b"
while data:
    matches = re.finditer(pattern, data)
    if matches:
        for site in matches:
            print(site.group())
    data = input()