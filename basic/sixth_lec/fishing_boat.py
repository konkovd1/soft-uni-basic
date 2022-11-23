budget = int(input())
season = input()
fishermen = int(input())

loan = 0
if season == 'Spring':
    loan = 3000
elif season == 'Summer' or season == 'Autumn':
    loan = 4200
else:
    loan = 2600

if fishermen <= 6:
    loan *= 0.9
elif fishermen <= 11:
    loan *= 0.85
else:
    loan *= 0.75

if fishermen % 2 == 0 and \
        (season == 'Spring' or
         season == 'Summer' or season == 'Winter'):
    loan *= 0.95

left_money = abs(budget - loan)
if budget >= loan:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {left_money:.2f} leva.")
