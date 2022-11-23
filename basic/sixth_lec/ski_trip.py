days = int(input())
type_accommodation = input()
grade = input()

sleepovers = days - 1
cost = 0
if type_accommodation == 'room for one person':
    cost = sleepovers * 18
elif type_accommodation == 'apartment':
    cost = sleepovers * 25
    if days < 10:
        cost *= 0.7
    elif days <= 15:
        cost *= 0.65
    else:
        cost *= 0.5
elif type_accommodation == 'president apartment':
    cost = sleepovers * 35
    if days < 10:
        cost *= 0.9
    elif days <= 15:
        cost *= 0.85
    else:
        cost *= 0.8
if grade == 'positive':
    cost *= 1.25
else:
    cost *= 0.9

print(f'{cost:.2f}')
