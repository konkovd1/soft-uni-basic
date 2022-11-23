iterations = int(input())

first_half = []
second_half = []

for i in range(iterations):
    first_half.append(int(input()))

for _ in range(iterations):
    second_half.append(int(input()))

if sum(first_half) == sum(second_half):
    print(f"Yes, sum = {sum(first_half)}")
else:
    print(f'No, diff = {abs(sum(first_half) - sum(second_half))}')
