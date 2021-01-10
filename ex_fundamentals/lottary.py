def symbol_count(ticket):
    count_first_half = 0
    count_second_half = 0
    match_symbol = None
    count = 0
    for symbol in special_symbols:
        index = 0
        while index < len(first_half):
            while first_half[index] == symbol and index < 10:
                count += 1
                index += 1
                if count > 5:
                    count_first_half = count
                    match_symbol = symbol
                if index == 10:
                    break
            if index < 10:
                index += 1
            count = 0
        index = 0
        while index < len(second_half):
            while second_half[index] == symbol and index < 10:
                count += 1
                index += 1
                if count > 5:
                    count_second_half = count
                    match_symbol = symbol
                if index == 10:
                    break
            if index < 10:
                index += 1
            count = 0

    if 5 < count_first_half <= 10 and 5 < count_second_half <= 10:
        if count_second_half == count_first_half and count_second_half < 10 and count_first_half < 10:
            return f'ticket "{ticket}" - {count_first_half}{match_symbol}'
        elif count_first_half == 10 and count_second_half == 10:
            return f'ticket "{ticket}" - {10}{match_symbol} Jackpot!'
        elif count_second_half > count_first_half:
            return f'ticket "{ticket}" - {count_first_half}{match_symbol}'
        elif count_second_half < count_first_half:
            return f'ticket "{ticket}" - {count_second_half}{match_symbol}'

    else:
        return f'ticket "{ticket}" - no match'


tickets = input().split(', ')

special_symbols = ['@', '#', '^', '$']
for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) == 20:
        first_half = ticket[:10]
        second_half = ticket[10:]
        print(symbol_count(ticket))

    else:
        print("invalid ticket")