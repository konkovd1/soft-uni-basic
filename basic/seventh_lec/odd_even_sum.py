iteration = int(input())

first_half = 0
second_half = 0
for i in range(iteration):
    number = int(input())
    if i % 2 == 0:
        first_half += number
    else:
        second_half += number

if first_half == second_half:
    print(f'Yes')
    print(f'Sum = {first_half}')
else:
    print('No')
    print(f'Diff = {abs(first_half - second_half)}')
