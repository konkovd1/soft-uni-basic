open_tabs = int(input())
salary = int(input())

for open_tab in range(open_tabs):
    name_of_the_tab = input()
    if name_of_the_tab == 'Facebook':
        salary -= 150
    elif name_of_the_tab == 'Instagram':
        salary -= 100
    elif name_of_the_tab == 'Reddit':
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)
