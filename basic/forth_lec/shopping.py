budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

total_video_cards = video_cards * 250
total_processors = total_video_cards * 0.35 * processors
total_ram = total_video_cards * 0.1 * ram
money_needed = total_processors + total_ram + total_video_cards

if video_cards > processors:
    money_needed *= 0.85

total = abs(money_needed - budget)

if budget >= money_needed:
    print(f"You have {total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total:.2f} leva more!")
