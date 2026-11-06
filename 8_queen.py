def is_safe(board, row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False

        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False

        i -= 1
        j += 1

    return True


def solve(board, row):

    # All queens are placed
    if row == len(board):
        return True

    for col in range(len(board)):

        if is_safe(board, row, col):

            board[row][col] = 'Q'

            if solve(board, row + 1):
                return True

            # Backtracking
            board[row][col] = '.'

    return False


# Main program
N = 8

board = [['.' for _ in range(N)] for _ in range(N)]

if solve(board, 0):
    print("8-Queens Solution:\n")

    for row in board:
        print(" ".join(row))
else:
    print("No solution exists")
