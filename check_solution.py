field = [
         "  ####   ",
         "###  ####",
         "#     $ #",
         "# #  #$ #",
         "# . .#P #",
         "#########"
]

field = [list(row) for row in field]

moves = ["u", "d", "l"]


def make_move(curr_pos: tuple, move: str) -> tuple:
    if move == "l":
        return curr_pos[0], curr_pos[1] - 1
    elif move == "r":
        return curr_pos[0], curr_pos[1] + 1
    elif move == "u":
        return curr_pos[0] - 1, curr_pos[1]
    elif move == "d":
        return curr_pos[0] + 1, curr_pos[1]
    else:
        return -1, -1  # every minus as position means player cheated


def find_player_and_goal(curr_field):
    p = ()
    g = []
    for row_index in range(len(curr_field)):
        for col_index in range(len(curr_field[row_index])):
            if curr_field[row_index][col_index] == "P":
                p = (row_index, col_index)
            if curr_field[row_index][col_index] == ".":
                g.append((row_index, col_index))
    return p, g


def eval_move(curr_field, pos, curr_move):
    curr_pos = curr_field[pos[0]][pos[1]]
    if curr_pos == "X":
        return -1, -1
    elif curr_pos == " " or curr_pos == "$":
        return pos
    elif curr_pos == ".":
        stone_pos = make_move(pos, curr_move)
        if
    else:
        return -1, -1


def workflow(game_field):
    player, goal_positions = find_player_and_goal(game_field)
    goal1_row, goal1_col = goal_positions[0]
    goal2_row, goal2_col = goal_positions[1]
    for move in moves:
        # wenn zielpunkte leer sind setzt ziel drauf
        if game_field[goal1_row][goal1_col] == " ":
            game_field[goal1_row][goal1_col] = "$"
        if game_field[goal2_row][goal2_col] == " ":
            game_field[goal2_row][goal2_col] = "$"

        next_pos = make_move(player, move)
        if next_pos[0] < 0 or next_pos[1] < 0:
            return False
        next_pos = eval_move(game_field, next_pos, move)
        if next_pos[0] < 0 or next_pos[1] < 0:
            return False
