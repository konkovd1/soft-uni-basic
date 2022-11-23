change_coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
given_input = float(input())

counter_coins = 0
while given_input > 0:
    for coin in range(len(change_coins)):
        given_input = round(given_input, 2)
        if given_input >= change_coins[coin]:
            counter_coins += 1
            given_input -= change_coins[coin]
            break

print(counter_coins)
