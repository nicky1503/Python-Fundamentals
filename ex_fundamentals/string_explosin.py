chars = input()
result = [i for i in chars]
final_result = []
power = 0
index = 0
for i in result:
    if i.isdigit():
        power += int(i)
    if i != '>' and power > 0:
        power -= 1
    else:
        final_result.append(i)
print(''.join(final_result))
