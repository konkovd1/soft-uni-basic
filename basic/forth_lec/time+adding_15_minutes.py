hour = int(input())
minutes = int(input())

added_fifteen_minutes = minutes + 15
if added_fifteen_minutes >= 60:
    hour += 1
    if hour > 23:
        hour = 0
    added_fifteen_minutes -= 60
    print(f"{hour}:{added_fifteen_minutes:02d}")
else:
    print(f"{hour}:{added_fifteen_minutes:02d}")
