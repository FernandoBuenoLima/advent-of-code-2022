#file = open("ex.txt")
file = open("input.txt")

rock = 'A'
paper = 'B'
scissors = 'C'

lose = 'X'
draw = 'Y'
win = 'Z'

rock_dict = {
    lose: scissors,
    draw: rock,
    win: paper
}

paper_dict = {
    lose: rock,
    draw: paper,
    win: scissors
}

scissors_dict = {
    lose: paper,
    draw: scissors,
    win: rock
}

results_dict = { rock: rock_dict, paper: paper_dict, scissors: scissors_dict }

match_result_list = [lose, draw, win]
results_to_index = [rock, paper, scissors]


shape_points = dict()
shape_points[rock] = 1
shape_points[paper] = 2
shape_points[scissors] = 3

points = 0

for line in file:
    data = line.split()

    opponent = data[0]
    match_result = data[1]

    player = results_dict[opponent][match_result]

    points += results_to_index.index(player) + 1
    points += match_result_list.index(match_result) * 3


print(points)
