class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return 
        def search(word, row, col,idx):
            if idx >= len(word):
                return True
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            
            if idx < len(word) and board[row][col] == word[idx]:
                temp = board[row][col]
                board[row][col] = "#"
                flag = search(word, row - 1, col, idx + 1) or search(word, row + 1, col, idx + 1) or search(word, row, col + 1, idx + 1) or search(word, row, col - 1, idx + 1)
                board[row][col] = temp
                return flag
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and search(word,i,j,0):
                    return True                
        return False
