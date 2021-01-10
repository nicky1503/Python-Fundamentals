class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment(input().split(), input())
print(comment.username)
print(list(comment.content))
print(comment.likes)


