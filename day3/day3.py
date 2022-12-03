with open('./day3/input.txt') as f:
    rucksacks = f.read().splitlines()

part1 = 0
for rucksack in rucksacks:
    firstCompartment, secondCompartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    match = [x for x in firstCompartment if x in secondCompartment].pop()
    part1 += ord(match)-38 if match.isupper() else ord(match)-96

part2 = 0 
for i in range(0, len(rucksacks), 3):
    match = [x for x in rucksacks[i] if x in rucksacks[i+1] and x in rucksacks[i+2]].pop()
    part2 += ord(match)-38 if match.isupper() else ord(match)-96

# Part 1
print("Part 1: {}".format(part1))

# Part 2
print("Part 2: {}".format(part2))