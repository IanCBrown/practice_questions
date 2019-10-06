import sys

def is_valid(board):
    k_count = 0 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "k":
                k_count += 1
                if "k" in get_neighbors(i, j, board):
                    return "invalid"

    if k_count == 9:
        return "valid"
    else:
        return "invalid"


def get_neighbors(row, col, board):
    k_array = []
    if row + 1 < len(board) and col + 2 < len(board[0]):
        k_array.append(board[row + 1][col + 2])
    if row + 1 < len(board) and col - 2 >= 0:
        k_array.append(board[row + 1][col - 2])
    if row - 1 >= 0 and col + 2 < len(board[0]):
        k_array.append(board[row - 1][col + 2])
    if row - 1 >= 0 and col - 2 >= 0: 
        k_array.append(board[row - 1][col - 2])

    if row + 2 < len(board) and col + 1 < len(board[0]):
        k_array.append(board[row + 2][col + 1])
    if row - 2 >= 0 and col + 1 < len(board[0]):
        k_array.append(board[row - 2][col + 1])
    if row + 2 < len(board) and col - 1 >= 0:
        k_array.append(board[row + 2][col - 1])
    if row - 2 >= 0 and col - 1 >= 0:
        k_array.append(board[row - 2][col - 1])
    return k_array

board = []
for line in sys.stdin.readlines():
    row = list(line.strip())
    board.append(row)

# for row in board:
#     print(row)
print(is_valid(board))