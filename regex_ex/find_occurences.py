import re
text = input().lower()
word = input().lower()
pattern = r"(^|(?<=\s))($|(?=\s))"

count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), text))
print(count)