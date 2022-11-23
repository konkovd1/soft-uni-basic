def if_goal_reached():
    if current_steps >= goal:
        print("Goal reached! Good job!")
        print(f"{abs(current_steps - goal)} steps over the goal!")
        return True
    if new_steps == 'Going home' and not current_steps >= goal:
        print(f"{abs(current_steps - goal)} more steps to reach goal.")


current_steps = 0
goal = 10000

while True:
    new_steps = input()
    if new_steps == 'Going home':
        current_steps += int(input())
        if_goal_reached()
        break
    current_steps += int(new_steps)
    if if_goal_reached():
        break
