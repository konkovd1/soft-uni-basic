number = int(input())

result = 0
for n in range(0, number + 1, 2):
    result = 2 ** n
    print(result)
