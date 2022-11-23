numbers = []

while True:
    number = input()
    if number == 'Stop':
        break
    numbers.append(int(number))

print(min(numbers))
