count_groups = int(input())

total_people = 0
group_musala = 0
group_monblan = 0
group_kilimandjaro = 0
group_k2 = 0
group_everest = 0

for _ in range(count_groups):
    people = int(input())
    if people <= 5:
        group_musala += people
    elif people <= 12:
        group_monblan += people
    elif people <= 25:
        group_kilimandjaro += people
    elif people <= 40:
        group_k2 += people
    else:
        group_everest += people
    total_people += people

print(f'{group_musala/total_people*100:.2f}%')
print(f'{group_monblan/total_people*100:.2f}%')
print(f'{group_kilimandjaro/total_people*100:.2f}%')
print(f'{group_k2/total_people*100:.2f}%')
print(f'{group_everest/total_people*100:.2f}%')
