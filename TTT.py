def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):

    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    player = "X"

    for turn in range(9):

        print_board(board)

        print(f"Player {player}'s turn")

        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        # Check valid position
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position!")
            continue

        # Check if position is already occupied
        if board[row][col] != " ":
            print("Position already occupied!")
            continue

        # Place player's symbol
        board[row][col] = player

        # Check winner
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            return

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

    print_board(board)
    print("It's a draw!")


tic_tac_toe()
