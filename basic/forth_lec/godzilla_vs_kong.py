budget_for_film = float(input())
statists = int(input())
price_per_statist = float(input())

decor = budget_for_film * 0.1
total_money_for_statists = statists * price_per_statist
if statists >= 150:
    total_money_for_statists *= 0.9

total_money = total_money_for_statists + decor
left_money = abs(budget_for_film - total_money)

if total_money > budget_for_film:
    print("Not enough money!")
    print(f"Wingard needs {left_money:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")
