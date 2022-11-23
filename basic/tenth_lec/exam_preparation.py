unsatisfied_grades = int(input())

fails = 0
average_score = 0
problems_solved = 0
last_problem = ''
while True:
    name_problem = input()
    if name_problem == "Enough":
        print(f'Average score: {average_score / problems_solved:.2f}')
        print(f'Number of problems: {problems_solved}')
        print(f'Last problem: {last_problem}')
        break
    evaluation = int(input())
    if evaluation <= 4:
        fails += 1
        if fails == unsatisfied_grades:
            print(f"You need a break, {fails} poor grades.")
            break
    average_score += evaluation
    problems_solved += 1
    last_problem = name_problem
