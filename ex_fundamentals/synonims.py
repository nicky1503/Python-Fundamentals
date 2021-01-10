num_of_lines = int(input())*2
words = {}
prev_word = None
for line in range(num_of_lines):
    synonyms = input()
    if line % 2 == 0:
        prev_word = synonyms
    if line % 2 == 1:
        if prev_word not in words:
            words[prev_word] = synonyms
        else:
            words[prev_word] += ', ' + synonyms

for k, v in words.items():
    print(f"{k} - {v}")
