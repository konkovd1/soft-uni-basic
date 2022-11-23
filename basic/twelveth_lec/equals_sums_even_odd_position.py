first_number = int(input())
second_number = int(input())

even_nums_sum = 0
odd_nums_sum = 0
for n in range(first_number, second_number + 1):
    the_number = str(n)
    counter = 0
    even_nums_sum = 0
    odd_nums_sum = 0
    for letter in the_number:
        if counter % 2 == 0:
            even_nums_sum += int(letter)
        else:
            odd_nums_sum += int(letter)
        counter += 1
    if even_nums_sum == odd_nums_sum:
        print(the_number, end=' ')
