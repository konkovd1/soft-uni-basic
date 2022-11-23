first_contestant = int(input())
second_contestant = int(input())
third_contestant = int(input())

total_time = first_contestant + second_contestant + third_contestant
minutes = 0
if total_time < 60:
    if total_time <= 9:
        print(f"0:0{total_time}")
    else:
        print(f"0:{total_time}")
else:
    while total_time >= 60:
        total_time -= 60
        minutes += 1
    if total_time <= 9:
        print(f"{minutes}:0{total_time}")
    else:
        print(f"{minutes}:{total_time}")
