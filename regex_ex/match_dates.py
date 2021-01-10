import re
data = input()
pattern = r"\b(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"
matches = re.finditer(pattern, data)
#splitters = re.findall(pattern, data)
for match in matches:
    match = match.groupdict()
    print(f"Day: {match['day']}, Month: {match['month']}, Year: {match['year']}")
    print(*match.values(), sep=', ')


