student_name = input()
grade = 1
total_score = 0
fails = 0
while not grade == 13:
    evaluation = float(input())
    if evaluation < 4:
        fails += 1
        if fails == 2:
            print(f"{student_name} has been excluded at {grade} grade")
            break
        continue
    total_score += evaluation
    grade += 1
if fails <= 1:
    print(f"{student_name} graduated. Average grade: {total_score / 12:.2f}")
