def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


prime_numbers = 0
non_prime_numbers = 0

while True:
    command = input()
    if command == 'stop':
        print(f"Sum of all prime numbers is: {prime_numbers}")
        print(f"Sum of all non prime numbers is: {non_prime_numbers}")
        break
    number = int(command)
    if number < 0:
        print("Number is negative.")
        continue
    if is_prime(number):
        prime_numbers += number
    else:
        non_prime_numbers += number
