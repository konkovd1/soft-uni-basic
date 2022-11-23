from math import pi

shape = input()

if shape == 'square' or shape == 'circle':
    number = float(input())
    if shape == 'square':
        print(f'{number * number:.3f}')
    else:
        print(f'{pi * number * number:.3f}')
else:
    first_num = float(input())
    second_num = float(input())
    if shape == 'rectangle':
        print(f'{first_num * second_num:.3f}')
    else:
        print(f'{first_num * second_num * 0.5:.3f}')
