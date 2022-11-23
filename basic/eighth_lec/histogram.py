number = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for n in range(number):
    input_number = int(input())
    if input_number < 200:
        p1_count += 1
    elif input_number < 400:
        p2_count += 1
    elif input_number < 600:
        p3_count += 1
    elif input_number < 800:
        p4_count += 1
    else:
        p5_count += 1

print(f'{p1_count / number * 100:.2f}%')
print(f'{p2_count / number * 100:.2f}%')
print(f'{p3_count / number * 100:.2f}%')
print(f'{p4_count / number * 100:.2f}%')
print(f'{p5_count / number * 100:.2f}%')
