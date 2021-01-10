import re
data = input()
pattern1 = r"\d"
pattern2 = r"(::|\*\*)([A-Z][a-z][a-z]+)\1"
cool_threshold = 1
emoji_count = 0
emojis = []
match_digits = re.findall(pattern1, data)
match_emojis = re.finditer(pattern2, data)
for digit in match_digits:
    cool_threshold *= int(digit)
print(f"Cool threshold: {cool_threshold}")

for e in match_emojis:
    emoji_count += 1
    emoji = e.group(2)
    cool_factor = [ord(factor) for factor in emoji]
    coolness = sum(cool_factor)
    if coolness > cool_threshold:
        emojis.append(e.group())

print(f"{emoji_count} emojis found in the text. The cool ones are:")
for em in emojis:
    print(em)