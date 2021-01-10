num_of_lines = int(input())
sum = 0
for letter in range(num_of_lines):
    char = input()
    sum += ord(char)
print(sum)

