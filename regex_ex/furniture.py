import re
data = input()
list2 = []
total_price = 0
print("Bought furniture:")
while data != "Purchase":
    pattern = r">>(?P<item>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+)"
    matches = re.finditer(pattern, data)
    for match in matches:
        print(match.group(1))
        price = match.group(2)
        quantity = match.group(3)
        total_price += float(price)*int(quantity)
    data = input()
print(f"Total money spend: {total_price:.2f}")