number = int(input())

counter_solutions = 0

for x in range(number + 1):
    for y in range(number + 2):
        for z in range(number + 2):
            if x + y + z == number:
                counter_solutions += 1

print(counter_solutions)
