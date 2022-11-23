from math import ceil

series = input()
length_of_episode = int(input())
length_of_lunch_break = int(input())

time_for_lunch = length_of_lunch_break * 0.125
time_for_break = length_of_lunch_break * 0.25

total_time = length_of_episode + time_for_lunch + time_for_break
left_time = ceil(abs(length_of_lunch_break - total_time))

if total_time <= length_of_lunch_break:
    print(f"You have enough time to watch {series} and left with {left_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {left_time} more minutes.")
