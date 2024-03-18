# n = int(input("Enter the value"))
n = 8
board = [[0 for i in range(n)] for i in range(n)]

def check_col(board, row, col):
    for i in range(row, -1, -1):
        if board[i][col] == 1:
            return False
    return True

def check_diagonal(board, row, col):
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def nqn(board, row):
    if row == n:
        return True

    for i in range(n):
        if (check_col(board, row, i) == True and
            check_diagonal(board, row, i) == True):
            board[row][i] = 1

            if nqn(board, row + 1):
                return True

            board[row][i] = 0

    return False

nqn(board, 0)

for row in board:
    print(row)