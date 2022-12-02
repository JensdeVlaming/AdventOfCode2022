part1 = 0
part2 = 0
    
with open('./day2/input.txt') as f:
    games = f.read().splitlines()

for game in games:
    options = game.split(" ")
    playerA = options[0]
    playerB = options[1]

    if playerA == "A" and playerB == "X":
        part1 += 4
        part2 += 3
    elif playerA == "A" and playerB == "Y":
        part1 += 8
        part2 += 4
    elif playerA == "A" and playerB == "Z":
        part1 += 3
        part2 += 8
    elif playerA == "B" and playerB == "X":
        part1 += 1
        part2 += 1
    elif playerA == "B" and playerB == "Y":
        part1 += 5
        part2 += 5
    elif playerA == "B" and playerB == "Z":
        part1 += 9
        part2 += 9
    elif playerA == "C" and playerB == "X":
        part1 += 7
        part2 += 2
    elif playerA == "C" and playerB == "Y":
        part1 += 2
        part2 += 6
    elif playerA == "C" and playerB == "Z":
        part1 += 6
        part2 += 7

# Part 1
print("Part 1: {}".format(part1))

# Part 2
print("Part 2: {}".format(part2))