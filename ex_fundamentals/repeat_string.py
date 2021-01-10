string = input()
num = int(input())


def repeat(text, repeat_count):
    result = ''
    for _ in range(repeat_count):
        result += text
    return result


print(repeat(string, num))
