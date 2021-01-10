prices = input()
final_sum = 0
while prices != 'special' and prices != 'regular':
    if float(prices) > 0:
        final_sum += float(prices)
    else:
        print("Invalid price!")
    prices = input()

if final_sum == 0:
    print("Invalid order!")
else:
    regular_c = final_sum*0.2
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {final_sum:.2f}$")

    if prices == 'special':
        print(f"Taxes: {regular_c:.2f}$")
        print("-----------")
        print(f"Total price: {(final_sum + regular_c)*0.9:.2f}$")

    elif prices == 'regular':
        print(f"Taxes: {regular_c:.2f}$")
        print("-----------")
        print(f"Total price: {final_sum + regular_c:.2f}$")
