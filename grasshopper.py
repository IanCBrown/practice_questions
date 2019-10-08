import sys
from collections import deque

# https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
# helpful result

def bfs(row,col, end_row, end_col, board):
    hops = 0
    if row == end_row and col == end_col:
        return hops
    
    visited = set()
    start = (row, col,board[row][col])
    q = deque()
    # q of paths
    q.append([start])

    while q:
        curr_path = q.popleft()
        # node = end of curr path
        node = curr_path[-1]
        if node[2] == 1:
            return curr_path
        if node not in visited:
            visited.add(node)
            neighbors = get_neighbors(node[0],node[1],board)
            for neighbor in neighbors:
                new_path = list(curr_path)
                new_path.append(neighbor)
                q.append(new_path)       
    return []


def get_neighbors(row, col, board):
    k_array = []
    if row + 1 < len(board) and col + 2 < len(board[0]):
        k_array.append((row + 1,col + 2,board[row + 1][col + 2]))
    if row + 1 < len(board) and col - 2 >= 0:
        k_array.append((row + 1,col - 2,board[row + 1][col - 2]))
    if row - 1 >= 0 and col + 2 < len(board[0]):
        k_array.append((row - 1,col + 2,board[row - 1][col + 2]))
    if row - 1 >= 0 and col - 2 >= 0: 
        k_array.append((row - 1,col - 2,board[row - 1][col - 2]))

    if row + 2 < len(board) and col + 1 < len(board[0]):
        k_array.append((row + 2,col + 1,board[row + 2][col + 1]))
    if row - 2 >= 0 and col + 1 < len(board[0]):
        k_array.append((row - 2,col + 1,board[row - 2][col + 1]))
    if row + 2 < len(board) and col - 1 >= 0:
        k_array.append((row + 2,col - 1,board[row + 2][col - 1]))
    if row - 2 >= 0 and col - 1 >= 0:
        k_array.append((row - 2,col - 1,board[row - 2][col - 1]))
    return k_array


for line in sys.stdin.readlines():
    line = line.split()
    n,m = int(line[0]), int(line[1])
    row,col = int(line[2]) - 1, int(line[3]) - 1
    end_row, end_col = int(line[4]) - 1, int(line[5]) - 1

    board = [[0 for i in range(n)] for x in range(m)]
    board[end_row][end_col] = 1 

    path = bfs(row,col,end_row,end_col,board)
    
    if len(path) == 0:
        print("impossible")
    else:
        # account for start state and subtract one
        print(len(path) - 1)