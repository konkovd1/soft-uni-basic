needed_money = float(input())
available_money = float(input())

counter = 0
only_spending = 0
while True:
    action = input()
    amount = float(input())
    counter += 1
    if action == 'spend':
        available_money -= amount
        only_spending += 1
        if only_spending == 5:
            print("You can't save the money.")
            print(counter)
            break
        if available_money < 0:
            available_money = 0
        continue
    else:
        available_money += amount
        only_spending = 0
    if available_money >= needed_money:
        print(f"You saved the money for {counter} days.")
        break
