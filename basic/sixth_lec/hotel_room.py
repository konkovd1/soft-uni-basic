month = input()
sleepovers = int(input())

total_studio = 0
total_apartment = 0

if month == 'May' or month == 'October':
    total_studio = sleepovers * 50
    total_apartment = sleepovers * 65
    if sleepovers > 14:
        total_studio *= 0.7
        total_apartment *= 0.9
    elif sleepovers > 7:
        total_studio *= 0.95
elif month == 'June' or month == 'September':
    total_studio = sleepovers * 75.2
    total_apartment = sleepovers * 68.7
    if sleepovers > 14:
        total_studio *= 0.8
        total_apartment *= 0.9
else:
    total_studio = sleepovers * 76
    total_apartment = sleepovers * 77
    if sleepovers > 14:
        total_apartment *= 0.9

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
