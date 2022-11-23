beginning_number = int(input())
ending_number = int(input())
magic_number = int(input())

combinations = []
found_combination = False

for x in range(beginning_number, ending_number + 1):
    for y in range(beginning_number, ending_number + 1):
        combinations.append((x, y))

for i in range(len(combinations)):
    if sum(combinations[i]) == magic_number:
        print(f'Combination N:{i + 1} ({combinations[i][0]} + '
              f'{combinations[i][1]} = {sum(combinations[i])})')
        found_combination = True
        break

if not found_combination:
    print(f'{len(combinations)} combinations - neither equals {magic_number}')
