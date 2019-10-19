class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        vertical_skyline = []
        horizontal_skyline = []  
        count = 0 
        
        for row in grid:
            horizontal_skyline.append(max(row))
        
        columns = list(zip(*grid))
        
        for col in columns:
            vertical_skyline.append(max(col))
            
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                while grid[row][col] < horizontal_skyline[row] and grid[row][col] < vertical_skyline[col]:
                    grid[row][col] += 1
                    count += 1
        return count
        
        