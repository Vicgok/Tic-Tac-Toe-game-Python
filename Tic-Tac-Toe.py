# Variables

board = ["$", "$", "$",
         "$", "$", "$",
         "$", "$", "$"]
game_active = True
winner = None
# let X start the game
active_player = "X"

# Display current board
def view_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# Start the game.
def start_game():

    # Display the board.
    view_board()

    # Loop for game to keep going.
    while game_active:
        
        turns(active_player)
        is_game_over()
        switch_player()

    # When game is over.
    if winner == "X" or winner == "O":
        print(winner + " won")
    elif winner == None:
        print("Tie")

# Handles turns for X and O
def turns(player):

    print(player + "'s turn")
    position = input("Choose a position(1-9):")

    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position = input("Choose a position(1-9):")

    position = int(position) - 1
    board[position] = player
    view_board()

# check is game is over
def is_game_over():
    
    player_won()
    is_a_tie()

# Check for winner.
def player_won():
    # To access global variable
    global winner

    row_winner = row_check()
    col_winner = column_check()
    diagonals_winner = diagonals_check()

    if row_winner:
        winner = row_check()
    elif col_winner:
        winner = column_check()
    elif diagonals_winner:
        winner = diagonals_check()
    return

# Row combination check.
def row_check():
    global game_active

    row_1 = board[0] == board[1] == board[2] != "$"
    row_2 = board[3] == board[4] == board[5] != "$"
    row_3 = board[6] == board[7] == board[8] != "$"

    if row_1 or row_2 or row_3:
        game_active = False
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

# Column cobination check
def column_check():
    global game_active

    col_1 = board[0] == board[3] == board[6] != "$"
    col_2 = board[1] == board[4] == board[7] != "$"
    col_3 = board[2] == board[5] == board[8] != "$"

    if col_1 or col_2 or col_3:
        game_active = False
    
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

# Diagonals check
def diagonals_check():
    global game_active

    diagonal_1 = board[0] == board[4] == board[8] != "$"
    diagonal_2 = board[2] == board[4] == board[6] != "$"

    if diagonal_1 or diagonal_2:
        game_active = False
    
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

# Check for tie
def is_a_tie():
    global game_active
    if "$" not in board:
        game_active = False
    return

# Switch X and O's turn
def switch_player():
    
    global active_player
    if active_player == "X":
        active_player = "O"
    elif active_player == "O":
        active_player = "X"
    return

# calling start game function to start the game
start_game()