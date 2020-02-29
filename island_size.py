class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    score = dfs(grid, i, j)
                    if score > max_area:
                        max_area = score
                        score = 0
        return max_area
    
    
def dfs(grid, row, col):
    # if grid[row][col] == 0:
    #     return 0
    score = 1
    
    grid[row][col] = 0
    if row - 1 >= 0 and grid[row - 1][col] == 1:
        score += 1
        dfs(grid, row - 1, col)
    if col - 1 >= 0 and grid[row][col - 1] == 1:
        score += 1
        dfs(grid, row, col - 1)
    if row + 1 < len(grid) and grid[row + 1][col] == 1:
        score += 1
        dfs(grid, row + 1, col)
    if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
        score += 1
        dfs(grid, row, col + 1)
    
    return score