file = open('input.txt', 'r')
contents = file.read().strip()
file.close()

def get_count(string, amount):
    count = 0
    for i in range(len(contents)-amount):
        temp = [x for x in contents[i:i+amount]]
        if sorted(temp) == sorted(list(set(temp))):
            count += amount
            return count
        else:
            count += 1

print("Part 1: ", get_count(contents, 4))
print("Part 2: ", get_count(contents, 14))
