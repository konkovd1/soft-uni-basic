excursion_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
fluffy_bears = int(input())
minion = int(input())
truck = int(input())

price_for_puzzles = puzzles * 2.6
price_for_talking_dolls = talking_dolls * 3
price_for_fluffy_bears = fluffy_bears * 4.1
price_for_minion = minion * 8.2
price_for_truck = truck * 2

total_ordered_toys = puzzles + talking_dolls + fluffy_bears + minion + truck

if total_ordered_toys >= 50:
    gathered_money = (price_for_puzzles + price_for_talking_dolls + price_for_fluffy_bears
                      + price_for_minion + price_for_truck) * 0.75
else:
    gathered_money = (price_for_puzzles + price_for_talking_dolls + price_for_fluffy_bears
                      + price_for_minion + price_for_truck)

total_saved_money = gathered_money * 0.9
left_money = abs(total_saved_money - excursion_price)

if total_saved_money >= excursion_price:
    print(f"Yes! {left_money:.2f} lv left.")
else:
    print(f"Not enough money! {left_money:.2f} lv needed.")
