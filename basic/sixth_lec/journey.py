budget = float(input())
season = input()

destination = ''
place = ''
cost = 0
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        cost = budget * 0.3
        place = 'Camp'
    else:
        cost = budget * 0.7
        place = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        cost = budget * 0.4
        place = 'Camp'
    else:
        cost = budget * 0.8
        place = 'Hotel'
else:
    destination = 'Europe'
    cost = budget * 0.9
    place = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{place} - {cost:.2f}')
