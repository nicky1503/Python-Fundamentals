words = input().lower().split()
words_uniques = list(dict.fromkeys(words))
words_dict = {}

for w in words_uniques:
    words_dict[w] = words.count(w)

for key, value in words_dict.items():
    if value % 2 == 1:
        print(key, end=' ')

