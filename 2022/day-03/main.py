file = open('input.txt', 'r')
contents = file.readlines()
file.close()

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

part_1, part_2 = 0, 0

for backpack in contents:
    first, second = set(backpack[:len(backpack)//2]), set(backpack[len(backpack)//2:])
    part_1 += letters.index(next(iter(first & second))) + 1

for i in range(0, len(contents), 3):
    first, second, third = set(contents[i].strip('\n')), set(contents[i+1].strip('\n')), set(contents[i+2].strip('\n'))
    part_2 += letters.index(next(iter(first & second & third))) + 1

print("Part 1: ", part_1)
print("Part 2: ", part_2)
