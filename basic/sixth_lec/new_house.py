type_flower = input()
number_flowers = int(input())
budget = int(input())

total_cost = 0
if type_flower == 'Roses':
    total_cost += 5 * number_flowers
    if number_flowers > 80:
        total_cost *= 0.9
elif type_flower == 'Dahlias':
    total_cost += 3.8 * number_flowers
    if number_flowers > 90:
        total_cost *= 0.85
elif type_flower == 'Tulips':
    total_cost += 2.8 * number_flowers
    if number_flowers > 80:
        total_cost *= 0.85
elif type_flower == 'Narcissus':
    total_cost += 3 * number_flowers
    if number_flowers < 120:
        total_cost *= 1.15
else:
    total_cost += 2.5 * number_flowers
    if number_flowers < 80:
        total_cost *= 1.2

left_money = abs(budget - total_cost)
if budget >= total_cost:
    print(f"Hey, you have a great garden with \
{number_flowers} {type_flower} and {left_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {left_money:.2f} leva more.")
