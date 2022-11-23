number = int(input())

used_numbers = number
incrementing = 0
for row in range(1, number+1):
    for col in range(row):
        incrementing += 1
        used_numbers -= 1

        print(incrementing, end=' ')
        if used_numbers <= 0:
            break
    if used_numbers <= 0:
        break
    print()
