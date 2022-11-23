width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height
taken_space = 0

while True:
    command = input()
    if command == 'Done':
        print(f"{free_space - taken_space} Cubic meters left.")
        break
    taken_space += int(command)
    if taken_space > free_space:
        print(f"No more free space! You need {taken_space - free_space} Cubic meters more.")
        break
