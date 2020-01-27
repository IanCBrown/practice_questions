class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(row, col, size):
            if grid[row][col] == 0:
                return size
            size += 1
            grid[row][col] = 0
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                # score += 1
                size = dfs(row - 1, col, size)
            if col - 1 >= 0 and grid[row][col - 1] == 1:
                # score += 1
                size = dfs(row, col - 1, size)
            if row + 1 < len(grid) and grid[row + 1][col] == 1:
                # score += 1
                size = dfs(row + 1, col, size)
            if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                # score += 1
                size = dfs(row, col + 1, size)

            return size
        
        max_area = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    score = dfs(i, j, 0)
                    if score > max_area:
                        max_area = score
                        score = 0
        return max_area
    
    

# [[1,1,0,1,1],
#  [1,0,0,0,0],
#  [0,0,0,0,1],
#  [1,1,0,1,1]]
