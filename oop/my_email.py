class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True
        return self.is_sent

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}'

convo = []
lines = input()
while lines != 'Stop':
    lines = lines.split(' ')
    sender, receiver, content = lines[0], lines[1], lines[2]
    email = Email(sender, receiver, content)
    convo.append(email.get_info())
    lines = input()

sent_indexes = input().split(', ')
print(sent_indexes)
for x in sent_indexes:
    print(f"{convo[int(x)]}. Sent: {email.send()}")