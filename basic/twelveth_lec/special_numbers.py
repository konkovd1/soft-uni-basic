number = int(input())

for n in range(1111, 10000):
    word = str(n)
    counter = 0
    for letter in word:
        if letter == '0':
            break
        if number % int(letter) == 0:
            counter += 1
        if counter == 4:
            print(n, end=' ')
number = int(input())
