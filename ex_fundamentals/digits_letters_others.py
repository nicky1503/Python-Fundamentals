data = input()
letters = ''
digits = ''
others = ''
for char in data:
    if char.isalpha():
        letters += letters.join(char)
    elif char.isdigit():
        digits += digits.join(char)
    else:
        others += others.join(char)

print(digits)
print(letters)
print(others)