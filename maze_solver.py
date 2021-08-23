import numpy as np

maze_loc = input("Give me the file name: ")

with open(str(maze_loc)+".txt", "r") as file:
    array_2D = [line.strip() for line in file]
    new_array = [list(line) for line in array_2D]
    longest = len(max(new_array, key=len))
    same_length_array = []
    for line in new_array:
        if len(line) < longest:
            line += " " * (longest - len(line))
        same_length_array.append(line)

maze = np.array(same_length_array)


def check_bounds(loc):
    bounds = np.shape(maze)
    # if 0 > loc[0] >= bounds[0] or 0 > loc[1] >= bounds[1]:
    #     return False
    # else:
    #     return True
    if 0 <= loc[0] < bounds[0] and 0 <= loc[1] < bounds[1]:
        return True
    else:
        return False


def move(loc, heading):
    if heading == "n":
        loc[1] -= 1
        values = {"left": [loc[0], loc[1] - 1], "ahead": [loc[0] - 1, loc[1]], "right": [loc[0], loc[1] + 1]}
        # values = [[loc[0], loc[1] - 1], [loc[0] - 1, loc[1]], [loc[0], loc[1] + 1]]
        new_headings = ["w", "n", "o"]
        return values, new_headings
    elif heading == "w":
        values = {"left": [loc[0] + 1, loc[1]], "ahead": [loc[0], loc[1] - 1], "right": [loc[0] + 1, loc[1]]}
        new_headings = ["s", "w", "n"]
        return values, new_headings
    elif heading == "s":
        values = {"left": [loc[0], loc[1] + 1], "ahead": [loc[0] + 1, loc[1]], "right": [loc[0], loc[1] - 1]}
        new_headings = ["o", "s", "w"]
        return values, new_headings
    elif heading == "o":
        values = {"left": [loc[0] - 1, loc[1]], "ahead": [loc[0], loc[1] + 1], "right": [loc[0] - 1, loc[1]]}
        new_headings = ["n", "o", "s"]
        return values, new_headings
# get value ( start end ) of 2d array and format it to a list [y, x] or [row, column]


def reverse(heading):
    if heading == "n":
        return "s"
    if heading == "w":
        return "o"
    if heading == "s":
        return "n"
    if heading == "o":
        return "w"


directions = ["n", "w", "s", "o"]

curr_direction = "n"  # starting direction
curr_loc = np.argwhere(maze == "S")[0].tolist()  # == start location
endpoint = np.argwhere(maze == "E")[0].tolist()

all_locations = [curr_loc]

while curr_loc != endpoint:
    turn_around = True
    possible_moves, headings = move(curr_loc, curr_direction)
    for index, position in enumerate(possible_moves.values()):
        if check_bounds(position):
            if maze.item(position[0], position[1]) in ["#", "E", "S"]:
                curr_loc = position
                curr_direction = headings[index]
                turn_around = False
                break

    if turn_around:
        new_direction = reverse(curr_direction)
        curr_direction = new_direction

    all_locations.append(curr_loc)

print(f"Way: {all_locations}")
print(endpoint)
print(curr_loc)