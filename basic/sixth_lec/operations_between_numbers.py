first_number = int(input())
second_number = int(input())
operator = input()

even_or_odd = ''
result = 0
if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    else:
        result = first_number * second_number
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{first_number} {operator} {second_number}'
          f' = {result} - {even_or_odd}')
elif operator == '/':
    if first_number == 0:
        print(f"Cannot divide {second_number} by zero")
    elif second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number / second_number
        print(f'{first_number} {operator} {second_number}'
              f' = {result:.2f}')
else:
    if first_number == 0:
        print(f"Cannot divide {second_number} by zero")
    elif second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number % second_number
        print(f'{first_number} {operator} {second_number}'
              f' = {result}')
