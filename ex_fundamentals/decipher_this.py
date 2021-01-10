string = input().split()
for index in range(len(string)):
    word = string[index]
    res = ''.join(filter(lambda is_num: is_num.isdigit(), word))
    word = word[len(res):]
    word = chr(int(res)) + word
    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    final_word = ''.join(word)
    print(final_word, end=' ' )