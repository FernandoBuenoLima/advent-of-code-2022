#file_name = 'ex.txt'
file_name = 'input.txt'

with open(file_name) as file:
    lines = [n.strip() for n in file.readlines()]

elves = []
elf = 0

for l in lines:
    if len(l) == 0:
        elves.append(elf)
        elf = 0
        continue
    elf += int(l)

elves.append(elf)
elves.sort()

print(elves[-1] + elves[-2] + elves[-3])

exit()
