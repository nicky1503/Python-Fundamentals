text = input()
result_string = ''
starting = 0
ending = 0
number = ''
result = ''
there_is_number = False
for letters in range(len(text)):
    for nums in text[letters:]:
        if nums.isdigit():
            number += nums
            there_is_number = True
        else:
            break
    if not text[letters].isdigit():
        result_string += text[letters].upper()
    if there_is_number:
            result += result_string*int(number)
            result_string = ''
            number = ''
    there_is_number = False
print(f"Unique symbols used: {len(set(result))}")
print(result)