height = int(input())
width = int(input())

cake_size = height * width
taken_cake = 0

while True:
    command = input()
    if command == 'STOP':
        print(f"{cake_size - taken_cake} pieces are left.")
        break
    taken_cake += int(command)
    if taken_cake > cake_size:
        print(f"No more cake left! You need {taken_cake - cake_size} pieces more.")
        break
