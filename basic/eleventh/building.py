floors = int(input())
rooms = int(input())

building = []
new = []
letter = ''
for f in range(floors, 0, -1):
    building.clear()
    for r in range(rooms):
        if f == floors:
            letter = 'L'
            building.append(f'{letter}{f}{r}')
        elif f % 2 == 0:
            letter = 'O'
            building.append(f'{letter}{f}{r}')
        else:
            letter = 'A'
            building.append(f'{letter}{f}{r}')
    new.append(building.copy())

for n in new:
    for i in range(len(n)):
        print(n[i], end=' ')
    print()

# counter = 0
# whole_building = ''
# for ap in building:
#     if counter == rooms:
#         whole_building += '\n' + ap + ' '
#         counter = 1
#         continue
#     whole_building += ap + ' '
#     counter += 1
# print(whole_building)
