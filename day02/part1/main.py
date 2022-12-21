#file = open("ex.txt")
file = open("input.txt")

opponent_rock = 'A'
opponent_paper = 'B'
opponent_scissors = 'C'

rock = 'X'
paper = 'Y'
scissors = 'Z'

results = dict()
results[opponent_rock] = (paper, rock)
results[opponent_paper] = (scissors, paper)
results[opponent_scissors] = (rock, scissors)

shape_points = dict()
shape_points[rock] = 1
shape_points[paper] = 2
shape_points[scissors] = 3

points = 0

for line in file:
    data = line.split()

    opponent = data[0]
    player = data[1]

    result = results[opponent]

    if result[0] == player:
        points += 6
    elif result[1] == player:
        points += 3

    points += shape_points[player]

print(points)
