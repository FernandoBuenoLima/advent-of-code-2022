from string import ascii_lowercase, ascii_uppercase

#file = open("ex.txt")
file = open("input.txt")

rucksacks = []
badges = []
priorities = ' ' + ascii_lowercase + ascii_uppercase

for line in file:
    rucksacks.append(line.strip())

i = 0
while i < len(rucksacks):
    b1 = set(rucksacks[i])
    b2 = set(rucksacks[i+1])
    b3 = set(rucksacks[i+2])

    badges.append([j for j in b1 if j in b2 and j in b3][0])

    i += 3

total = 0

for b in badges:
    total += priorities.rindex(b)

print(total)
