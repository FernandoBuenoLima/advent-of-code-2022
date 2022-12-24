#file = open('ex.txt')
file = open('input.txt')

def range_to_list(r):
    a, b = r.strip().split('-')
    a, b = int(a), int(b)
    l = list()
    for i in range(a, b+1):
        l.append(i)
    return l

pairs = list()
total = 0

for line in file:
    a, b = line.strip().split(',')
    a, b = range_to_list(a), range_to_list(b)
    if all(i in a for i in b) or all(i in b for i in a):
        total += 1

print(total)