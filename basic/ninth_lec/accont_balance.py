payment = input()
total = 0
while not payment == 'NoMoreMoney':
    payment = float(payment)
    if payment <= 0:
        print('Invalid operation!')
        break
    total += payment
    print(f'Increase: {payment:.2f}')
    payment = input()

print(f'Total: {total:.2f}')
