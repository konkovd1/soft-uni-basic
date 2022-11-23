lili_years = int(input())
washing_machine = float(input())
price_toy = int(input())

count_toys = 0
received_money = 0
increasing_money_per_year = 0
brother_stolen_money = 0
for year in range(1, lili_years + 1):
    if year % 2 == 0:
        brother_stolen_money -= 1
        increasing_money_per_year += 10
        received_money += increasing_money_per_year
    else:
        count_toys += 1

sold_toys = count_toys * price_toy
total_received_money = sold_toys + received_money + brother_stolen_money
left_money = abs(washing_machine - total_received_money)

if total_received_money >= washing_machine:
    print(f'Yes! {left_money:.2f}')
else:
    print(f'No! {left_money:.2f}')
