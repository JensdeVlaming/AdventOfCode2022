elves = [0]
    
with open('./day1/input.txt') as f:
    total = f.read().splitlines()

for calories in total:
    if calories.strip() == "":
        elves.append(0)
    else:
        elves[len(elves)-1] += int(calories)

# Part 1
print("Elf with highest calories: {}".format(max(elves)))

# Part 2
list.sort(elves)
print("Sum of top 3 elves with highest calories: {}".format(sum(elves[-3:])))