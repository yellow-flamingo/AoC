file = open('input.txt', 'r')
contents = file.readlines()
file.close()

part_1, part_2 = 0, 0

for pair in contents:
    list_first = []
    list_second = []
    data = pair.strip('\n').split(',')
    data_1, data_2 = data[0].split('-'), data[1].split('-')

    for i in range(int(data_1[0]), int(data_1[1])+1):
        list_first.append(i)
    for i in range(int(data_2[0]), int(data_2[1])+1):
        list_second.append(i)

    if set(list_first) <= set(list_second) or set(list_second) <= set(list_first):
        part_1 += 1

    if any(element in list_first for element in list_second):
        part_2 += 1


print("Part 1: ", part_1)
print("Part 2: ", part_2)
