# import sys
#
# iterations = int(input())
# max_number = -sys.maxsize
# count = 0
# for i in range(iterations):
#     number = int(input())
#     if number > max_number:
#         max_number = number
#     count += number
#
# count -= max_number
# if count == max_number:
#     print('Yes')
#     print(f'Sum = {max_number}')
# else:
#     print('No')
#     print(f'Diff = {abs(count - max_number)}')

iterations = int(input())
my_list = []
for i in range(iterations):
    my_list.append(int(input()))

my_list.sort(reverse=True)
max_num = my_list.pop(0)
if max_num == sum(my_list):
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print(f'Diff = {abs(sum(my_list)-max_num)}')
