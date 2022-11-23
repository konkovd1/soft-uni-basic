hour = int(input())
day = input()

working_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday']
working = False
if 10 <= hour <= 18:
    for working_day in working_days:
        if working_day == day:
            print('open')
            working = True
            break
    if not working:
        print('closed')
else:
    print('closed')
