n = int(input())
filter_word = input()
strings = []
filtered_string = []
for _ in range(n):
    user_input = input()
    strings.append(user_input)
for index in range(n):
    filter_word_count = strings[index].count(filter_word)
    if filter_word_count > 0:
        filtered_string.append(strings[index])

print(strings)
print(filtered_string)
