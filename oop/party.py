class Party:
    def __init__(self):
        self.party = []


names = Party()
people = input()
while people != 'End':
    names.party.append(people)
    people = input()
print(f"Going: {', '.join(names.party)}")
print(f"Total: {len(names.party)})")
