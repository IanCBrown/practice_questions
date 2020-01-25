class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        starting_color = image[sr][sc]
        image = dfs(image, newColor, starting_color, sr, sc)
        return image
        
def dfs(image, new_color, old_color, row, col):
    if image[row][col] == new_color:
        return image
    
    if image[row][col] == old_color:
        image[row][col] = new_color
        if row > 0 and image[row - 1][col] == old_color:
            dfs(image, new_color, old_color, row - 1, col)
        if col > 0 and image[row][col - 1] == old_color:
            dfs(image, new_color, old_color, row, col - 1)
        if row < len(image) - 1 and image[row + 1][col] == old_color:
            dfs(image, new_color, old_color, row + 1, col)
        if col < len(image[0]) - 1 and image[row][col + 1] == old_color:
            dfs(image, new_color, old_color, row, col + 1)
        
    return image
        
        
# get the initial color 
# consider the sp's 4 neighbors 
# if that neighbor is valid and it's color is equal to the old_color
# visit it and change it's color to the new color 