type_projection = input()
rows = int(input())
columns = int(input())

total_income = rows * columns
if type_projection == 'Premiere':
    total_income *= 12
elif type_projection == 'Normal':
    total_income *= 7.5
else:
    total_income *= 5

print(f'{total_income} leva')
