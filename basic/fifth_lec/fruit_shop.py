fruit = input()
day = input()
quantity = float(input())

error = False

cost = quantity
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or \
        day == 'Friday':
    if fruit == 'banana':
        cost *= 2.5
    elif fruit == 'apple':
        cost *= 1.2
    elif fruit == 'orange':
        cost *= 0.85
    elif fruit == 'grapefruit':
        cost *= 1.45
    elif fruit == 'kiwi':
        cost *= 2.7
    elif fruit == 'pineapple':
        cost *= 5.5
    elif fruit == 'grapes':
        cost *= 3.85
    else:
        error = True
        print('error')
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        cost *= 2.7
    elif fruit == 'apple':
        cost *= 1.25
    elif fruit == 'orange':
        cost *= 0.9
    elif fruit == 'grapefruit':
        cost *= 1.6
    elif fruit == 'kiwi':
        cost *= 3
    elif fruit == 'pineapple':
        cost *= 5.6
    elif fruit == 'grapes':
        cost *= 4.2
    else:
        error = True
        print('error')
else:
    error = True
    print('error')

if not error:
    print(f'{cost:.2f}')
