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
    board[row_input][column_input] = symbol_input
    return board

def start_game():
    symbol_input = None

    while True: 
        symbol_input = input("Choose the symbol for player 1 (O/X): ")
        if symbol_input.upper() in ["O","X"]: #can i turn this check into try except maybe?
            break
        else: 
            print("Invalid input")

    return symbol_input






board = [[" "," "," "],[" "," "," "],[" "," "," "]]
turn_number = 0
symbol_input = start_game()

while True:
    print("")
    print_board(board)
    print("")

    row_input, column_input = get_position()
    board = update_board(board, row_input, column_input, symbol_input)
    turn_number += 1

    if symbol_input == "O":
        symbol_input = "X"
    else:
        symbol_input = "O"

    if turn_number >= 2: #checks if someone won the game after three turns
        pass
        






