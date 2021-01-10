items = input().split('|')
budget = float(input())
profit_list = []
overall_profit = 0
for item in items:
    piece_of_clothing, price = item.split('->')
    price = float(price)
    if piece_of_clothing == 'Clothes' and price <= 50:
        if budget >= price:
            budget -= price
            profit_list.append(price*1.4)
            overall_profit += price*0.4
    if piece_of_clothing == 'Shoes' and price <= 35:
        if budget >= price:
            budget -= price
            profit_list.append(price * 1.4)
            overall_profit += price * 0.4
    if piece_of_clothing == 'Accessories' and price <= 20.5:
        if budget >= price:
            budget -= price
            profit_list.append(price * 1.4)
            overall_profit += price * 0.4
for profit_per_item in profit_list:
    print(f'{profit_per_item:.2f} ', end='')
print(f'\nProfit: {overall_profit:.2f}')
if budget + sum(profit_list) >= 150:
    print('Hello, France!')
else:
    print('Time to go.')

