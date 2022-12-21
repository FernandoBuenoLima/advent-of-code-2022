from string import ascii_lowercase, ascii_uppercase

#file = open("ex.txt")
file = open("input.txt")

repeated = []
priorities = ' ' + ascii_lowercase + ascii_uppercase

for line in file:
    line = line.strip()
    l = len(line)

    r1 = set(line[:(l//2)])
    r2 = set(line[l//2:])

    repeated.append([i for i in r1 if i in r2][0])

total = 0

for r in repeated:
    total += priorities.rindex(r)

print(total)
