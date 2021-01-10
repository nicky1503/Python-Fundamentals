user_input = input().split()
searched_palindrome = input()
result = [word for word in user_input if word == word[::-1]]
print(result)
print(f'Found palindrome {result.count(searched_palindrome)} times')
