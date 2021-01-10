data = input()
sides = {}
while data != "Lumpawaroo":
    try:
        user, side = data.split(' | ')
        
    except ValueError:
        pass
    try:
        user, side = data.split(' -> ')
    except ValueError:
        pass

