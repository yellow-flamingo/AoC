file = open('input.txt', 'r')
contents = file.readlines()
file.close()

opponent = ['A', 'B', 'C']
you = ['X', 'Y', 'Z']

scores = {'X': 1, 'Y': 2, 'Z': 3}

part_1, part_2 = 0, 0

for line in contents:
    data = line.strip('\n').split(' ')
    if opponent.index(data[0]) == you.index(data[1]):
        part_1 += 3
    elif (opponent.index(data[0])+1) % 3 == you.index(data[1]):
        part_1 += 6

    part_1 += scores.get(data[1])

    if data[1] == 'Y':
        part_2 += 3 + scores.get(you[opponent.index(data[0])])
    elif data[1] == 'Z':
        part_2 += 6 + scores.get(you[(opponent.index(data[0])+1) % 3])
    elif data[1] == 'X':
        part_2 += scores.get(you[(opponent.index(data[0])-1) % 3])

print("Part 1: ", part_1)
print("Part 2: ", part_2)
