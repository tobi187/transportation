field = [
         "  ####   ",
         "###  ####",
         "#     $ #",
         "# #  #$ #",
         "# . .#P #",
         "#########"
]

field = [list(row) for row in field]

moves_for_one_stone_left = ["r", "u", "u", "l", "l", "l", "u", "l", "d", "d", "r", "d", "l"]                            # ca 23 stelle
moves = ["r", "u", "u", "l", "l", "l", "u", "l", "d", "r", "r", "r", "r", "d", "d", "l", "u", "r", "u", "l", "l", "l", "d", "d", "l", "l", "l", "u", "u", "r", "r", "d", "r", "d", "l", "u", "u", "u", "r", "d", "d"]

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
    
    if curr_pos == "#":
        return -1, -1
    
    elif curr_pos == " " or curr_pos == ".":
        return pos
    
    elif curr_pos == "$":
        stone_pos_row, stone_pos_col = make_move(pos, curr_move)
        
        if curr_field[stone_pos_row][stone_pos_col] == "#" or curr_field[stone_pos_row][stone_pos_col] == "$":  # wird angenommen dass immer nur 1 stein geschoben werden kann (falls 2 hinterinander stehen kann man nicht schieben)
            return -1, -1
        
        else:
            return stone_pos_row, stone_pos_col
    
    else:
        return -1, -1


def workflow(game_field):
    player, goal_positions = find_player_and_goal(game_field)
    goal1_row, goal1_col = goal_positions[0]
    goal2_row, goal2_col = goal_positions[1]
    
    for index, move in enumerate(moves):
        # wenn zielpunkte leer sind setzt ziel drauf
        for goal_position in goal_positions:
            if game_field[goal_position[0]][goal_position[1]] == " ":
                game_field[goal_position[0]][goal_position[1]] == "." 

        # fuehre naechsten zug aus und gib neue position zuruek
        next_pos = make_move(player, move)
        if next_pos[0] < 0 or next_pos[1] < 0:
            return False
        
        # check ob naechste postion kein X ist
        # wenn naechste position ein . ist fuehre dieses und vorherige funktion nochmal fuer punkt aus
        stone_or_next_pos = eval_move(game_field, next_pos, move)
        if stone_or_next_pos[0] < 0 or stone_or_next_pos[1] < 0:
            return False
        
        # wenn moves legal sind schiebe spieler 1 feld in moverichting mach altes feld zu leerem feld
        game_field[player[0]][player[1]] = " "
        game_field[next_pos[0]][next_pos[1]] = "P"

        # wenn spieler stein geschoben hat setze stein ein feld weiter
        if next_pos != stone_or_next_pos:
            game_field[stone_or_next_pos[0]][stone_or_next_pos[1]] = "$"
        
        # setze neue spielerposition
        player = next_pos


    for goal_position in goal_positions:
        if game_field[goal_position[0]][goal_position[1]] != "$":
            return False
    return True 

print(workflow(field))
