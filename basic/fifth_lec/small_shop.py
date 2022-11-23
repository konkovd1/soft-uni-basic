product = input()
city = input()
quantity = float(input())

cost = quantity
if city == 'Sofia':
    if product == 'coffee':
        cost *= 0.5
    elif product == 'water':
        cost *= 0.8
    elif product == 'beer':
        cost *= 1.2
    elif product == 'sweets':
        cost *= 1.45
    else:
        cost *= 1.6
elif city == 'Plovdiv':
    if product == 'coffee':
        cost *= 0.4
    elif product == 'water':
        cost *= 0.7
    elif product == 'beer':
        cost *= 1.15
    elif product == 'sweets':
        cost *= 1.30
    else:
        cost *= 1.5
else:
    if product == 'coffee':
        cost *= 0.45
    elif product == 'water':
        cost *= 0.7
    elif product == 'beer':
        cost *= 1.10
    elif product == 'sweets':
        cost *= 1.35
    else:
        cost *= 1.55

print(cost)
