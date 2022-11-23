actor = input()
points_from_academy = float(input())
number_of_judges = int(input())

points_received = points_from_academy
for _ in range(number_of_judges):
    judge_name = input()
    points_from_judge = float(input())
    points_received += points_from_judge * len(judge_name) / 2
    if points_received >= 1250.5:
        print(f'Congratulations, {actor} got a nominee for leading role with {points_received:.1f}!')
        break

if points_received < 1250.5:
    print(f"Sorry, {actor} you need {1250.5 - points_received:.1f} more!")
