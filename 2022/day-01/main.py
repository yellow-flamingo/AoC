file = open('input.txt', 'r')
contents = file.readlines()
file.close()

values = []

count = 0
for line in contents:
    data = line.strip('\n')
    if data == '':
        values.append(count)
        count = 0
    else:
        count += int(data)

values.sort(reverse=True)

print("Part 1: ", max(values))
print("Part 2: ", sum(values[:3]))
