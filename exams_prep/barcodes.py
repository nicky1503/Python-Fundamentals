import re
n = int(input())
pattern = r"(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)"
barcodes = []
for _ in range(n):
    barcode = input()
    match = re.match(pattern, barcode)
    if not match:
        print("Invalid barcode")
    if match:
        code = match.group(2)
        code = [d for d in code if d.isdigit()]
        if len(code)> 0:
            print(f"Product group: {''.join(code)}")
        else:
            print("Product group: 00")


