data = input().split()
for i in range(len(data)):
    print(''.join(data[i])*len(data[i]), end='')