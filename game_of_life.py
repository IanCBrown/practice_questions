class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        copy = [[board[m][n] for n in range(len(board[0]))] for m in range(len(board))]
        # alive = [[0 for n in range(len(board[0]))] for m in range(len(board))]
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                curr = alive_neighbor_count(copy,r,c)
                # alive[r][c] = curr
                if copy[r][c] == 1 and curr < 2:
                    board[r][c] = 0
                elif copy[r][c] == 1 and (curr == 2 or curr == 3):
                    board[r][c] = 1
                elif copy[r][c] == 1 and curr > 3:
                    board[r][c] = 0 
                elif copy[r][c] == 0 and curr == 3:
                    board[r][c] = 1  
        # print(alive)
                
def alive_neighbor_count(board, row, col):
    count = 0 
    
    if row - 1 >= 0 and board[row - 1][col] == 1:
        count += 1
    if col - 1 >= 0 and board[row][col - 1] == 1:
        count += 1
    if row + 1 < len(board) and board[row + 1][col] == 1:
        count += 1
    if col + 1 < len(board[0]) and board[row][col + 1] == 1:
        count += 1
    if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] == 1:
        count += 1
    if row - 1 >= 0 and col + 1 < len(board[0]) and board[row - 1][col + 1] == 1:
        count += 1
    if row + 1 < len(board) and col - 1 >= 0 and board[row + 1][col - 1] == 1:
        count += 1
    if row + 1 < len(board) and col + 1 < len(board[0]) and board[row + 1][col + 1] == 1:
        count += 1
        
    return count
