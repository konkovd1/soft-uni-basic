number_of_judges = int(input())
final_score = 0
exams = 0
while True:
    presentation = input()
    if presentation == 'Finish':
        break
    exams += 1
    average_score = 0
    for judge in range(number_of_judges):
        evaluation = float(input())
        average_score += evaluation
    final_score += average_score / number_of_judges
    print(f'{presentation} - {average_score / number_of_judges:.2f}.')
print(f"Student's final assessment is {final_score / exams:.2f}.")
