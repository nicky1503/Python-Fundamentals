ints = input()
intigers = list(ints.split(' '))
reverse = []
for index in range(len(intigers)):
    if intigers[index].count('-') > 0:
        reverse.append(intigers[index].replace('-', ''))
    else:
        reverse.append('-' + intigers[index])
print(reverse)