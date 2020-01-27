class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if len(grid) <= 1:
            return 0
            
        count = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0: 
                    count += dfs(r, c, grid)  
                    
        return count
    
    
def dfs(row, col, grid):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return 0
    
    if grid[row][col] == 1:
        return 1
    
    grid[row][col] = 1
    up = dfs(row - 1, col, grid)
    left = dfs(row, col - 1, grid)
    down = dfs(row + 1, col, grid)
    right = dfs(row, col + 1, grid)
    
    if up == left == down == right == 1:
        return 1
    else:
        return 0
    
