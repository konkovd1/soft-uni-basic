from math import floor

count_tournaments = int(input())
start_points = int(input())

total_points = 0
wins = 0

for tournament in range(count_tournaments):
    reached_stage = input()
    if reached_stage == 'W':
        total_points += 2000
        wins += 1
    elif reached_stage == 'F':
        total_points += 1200
    else:
        total_points += 720

print(f'Final points: {total_points + start_points}')
print(f'Average points: {floor(total_points / count_tournaments)}')
print(f'{wins / count_tournaments * 100:.2f}%')
