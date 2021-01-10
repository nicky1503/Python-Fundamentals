data = input().split()
text = ''.join(data)
letter_count = {}
for char in text:
    if char not in letter_count:
        letter_count[char] = text.count(char)
for k, v in letter_count.items():
    print(f"{k} -> {v}")