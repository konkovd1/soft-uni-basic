total_student_tickets = 0
total_standard_tickets = 0
total_kid_tickets = 0
total_tickets = 0

while True:
    command = input()
    if command == "Finish":
        break
    free_space = int(input())
    occupied_space = 0
    student_tickets = 0
    standard_tickets = 0
    kid_tickets = 0
    while free_space > occupied_space:
        occupied_space += 1
        ticket = input()
        if ticket == 'End':
            break
        elif ticket == 'student':
            student_tickets += 1
        elif ticket == 'standard':
            standard_tickets += 1
        elif ticket == 'kid':
            kid_tickets += 1
    sold_tickets = student_tickets + standard_tickets + kid_tickets
    print(f'{command} - {sold_tickets / free_space * 100:.2f}% full.')
    total_tickets += sold_tickets
    sold_tickets = 0
    total_student_tickets += student_tickets
    total_standard_tickets += standard_tickets
    total_kid_tickets += kid_tickets

print(f'Total tickets: {total_tickets}')
print(f'{total_student_tickets / total_tickets * 100:.2f}% student tickets.')
print(f'{total_standard_tickets / total_tickets * 100:.2f}% standard tickets.')
print(f'{total_kid_tickets / total_tickets * 100:.2f}% kids tickets.')
