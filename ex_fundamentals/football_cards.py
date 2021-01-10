cards = list(input().split(' '))
team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for index_cards in range(len(cards)):
    if cards[index_cards].startswith('A'):
        if int(cards[index_cards][2:]) in team_A:
            team_A.remove(int(cards[index_cards][2:]))
    elif cards[index_cards].startswith('B'):
        if int(cards[index_cards][2:]) in team_B:
            team_B.remove(int(cards[index_cards][2:]))
    if len(team_A) < 7 or len(team_B) < 7:
        break
if len(team_A) < 7 or len(team_B) < 7:
    print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')
    print('Game was terminated')
elif len(team_A) >= 7 and len(team_B) >= 7:
    print(f'Team A - {len(team_A)}; Team B - {len(team_B)}')
