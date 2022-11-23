day = input()
working_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
not_error = True
for n in working_day:
    if day == n:
        print('Working day')
        break
    elif day == "Saturday" or day == "Sunday":
        print('Weekend')
        break
    elif n == working_day[-1]:
        print('Error')
