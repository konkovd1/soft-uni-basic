rotations = int(input())

numbers = []

for i in range(rotations):
    numbers.append(int(input()))

print(f'Max number: {max(numbers)}')
print(f'Min number: {min(numbers)}')
