def chars_in_range(first_char, second_char):
    charecters = ''
    for num in range(ord(first_char)+1, ord(second_char)):
        charecters += chr(num) + ' '
    return charecters


first_char = input()
second_char = input()
print(chars_in_range(first_char, second_char))