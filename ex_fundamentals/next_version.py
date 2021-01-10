start_version = list(map(int, input().split('.')))
if start_version[2] < 9:
    start_version[2] += 1
if start_version[2] == 9:
    start_version[2] = 0
    start_version[1] += 1
if start_version[1] > 8:
    start_version[1] = 0
    start_version[0] += 1
result = ''.join([str(num)+'.' for num in start_version])

print(result[:len(result)-1])