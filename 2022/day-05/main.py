file = open('input.txt', 'r')
contents = file.readlines()
file.close()

num_of_stacks = 0

# Split the input into stacks and instructions
stacks = [line.strip('\n') for line in contents[:contents.index('\n')]]
instructions = [(int(instr[1]), int(instr[3]), int(instr[5])) for instr in [instr.split() for instr in contents[(contents.index('\n')+1):]]]

# Get the total number of stacks
for num in stacks[-1].split():
    num_of_stacks += 1
stacks.pop()

# Create empty lists to hold the stacks
part_1_stacks = [[] for i in range(num_of_stacks)]
part_2_stacks = [[] for i in range(num_of_stacks)]


# Transpose the stack rows into the correct stacks
for row in stacks:
    stack_count = 0
    space_count = 0
    for i in range(len(row)):
        if row[i] == ' ':
            space_count += 1
            if space_count == 4:
                stack_count += 1
                space_count = 0
        elif row[i] == '[':
            space_count = 0
            part_1_stacks[stack_count].insert(0, row[i+1])
            part_2_stacks[stack_count].insert(0, row[i+1])
            stack_count += 1


# Follow the instructions to get the final stacks
for instr in instructions:
    move_count = 0
    for i in range(instr[0]):
        to_move_1 = part_1_stacks[instr[1]-1].pop()
        to_move_2 = part_2_stacks[instr[1]-1].pop()
        move_count += 1
        part_1_stacks[instr[2]-1].append(to_move_1)
        part_2_stacks[instr[2]-1].insert(len(part_2_stacks[instr[2]-1])-i, to_move_2)


part_1 = ''.join(stack[-1] for stack in part_1_stacks)
part_2 = ''.join(stack[-1] for stack in part_2_stacks)

print("Part 1: ", part_1)
print("Part 2: ", part_2)
