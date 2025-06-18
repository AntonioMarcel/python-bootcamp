def print_board(board):
    for k, row in enumerate(board):
        print(f"{row[0]} | {row[1]} | {row[2]}" )
        if k != 2:
            print("---------")

def get_position():    
    row_input = None
    column_input = None

    while True:
        try:
            row_input = int(input("Which row? "))
            break
        except ValueError:
            print("Invalid input.")

    while True:
        try:
            column_input = int(input("Which column? "))
            break
        except ValueError:
            print("Invalid input.")

    return row_input, column_input

def update_board(board, row_input, column_input, symbol_input):
    if not board[row_input][column_input].strip():
        board[row_input][column_input] = symbol_input
        return board
    else:
        print("")
        raise Exception("Invalid position")

def start_game():
    symbol_input = None

    while True: 
        symbol_input = input("Choose the symbol for player 1 (O/X): ")
        symbol_input = symbol_input.upper()
        if symbol_input in ["O","X"]: #can i turn this check into try except maybe?
            break
        else: 
            print("Invalid input")

    return symbol_input

def check_answers(turn_number, board):
    # Checks if someone won the game after minimun of three turns
    if turn_number >= 2:  
        # Check rows
        if any("".join(row) in ["OOO", "XXX"] for row in board):
            print("True")
            return True

        # Check columns        
        k = 0
        while k < len(board[0]):
            col_string = ""
            for row in board:
                col_string += row[k]
            if col_string in ["OOO", "XXX"]:
                #print(col_string)
                print("True")
                return True
            k +=1

        # Check diagonals
        main_diag = "".join([board[0][0],board[1][1], board[2][2]])
        anti_diag = "".join([board[0][2],board[1][1], board[2][0]])
        if main_diag in ["OOO","XXX"]:
            print("True")
            return True
        elif anti_diag in ["OOO","XXX"]:
            print("True")
            return True
    
    # If no answer after last turn, return True and finish the game
    if turn_number == 9:
        print("No contest")
        return True 
    
    # If no answer found, return False and continue the game
    return False

def game():
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    turn_number = 0
    symbol_input = start_game()

    while True:
        # Draws the board
        print("")
        print_board(board)
        print("")

        is_winner = check_answers(turn_number, board)

        if is_winner:
            break
        
        # Gets position inputs and updates the board
        row_input, column_input = get_position()
        try:
            board = update_board(board, row_input, column_input, symbol_input)
        except Exception as e:
            print(f"{e}")
            continue
    
        turn_number += 1

        # Changes player symbol
        if symbol_input == "O":
            symbol_input = "X"
        else:
            symbol_input = "O"

        
game()


