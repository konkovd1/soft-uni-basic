time_for_exam_hour = int(input())
time_for_exam_minutes = int(input())
time_of_arrival_hour = int(input())
time_of_arrival_minutes = int(input())

total_time_exam = time_for_exam_hour * 60 + time_for_exam_minutes
total_time_arrival = time_of_arrival_hour * 60 + time_of_arrival_minutes
delay_hours = abs(total_time_exam - total_time_arrival) // 60
delay_minutes = abs(total_time_exam - total_time_arrival) % 60

if total_time_arrival > total_time_exam:
    print('Late')
    if delay_hours == 0:
        print(f'{delay_minutes} minutes after the start')
    else:
        print(f'{delay_hours}:{delay_minutes:02d} hours after the start')
elif total_time_arrival == total_time_exam:
    print('On time')
else:
    if delay_hours == 0 and delay_minutes <= 30:
        print('On time')
        print(f'{delay_minutes} minutes before the start')
    elif delay_hours == 0 and delay_minutes > 30:
        print('Early')
        print(f'{delay_minutes} minutes before the start')
    else:
        print('Early')
        print(f'{delay_hours}:{delay_minutes:02d} hours before the start')

