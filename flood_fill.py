class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        color = image[sr][sc]
        if color == newColor:
            return image
        dfs(image, sr, sc, color, newColor)
        return image
                
def dfs(image, r, c, color, newColor):    
    if image[r][c] == color:
        image[r][c] = newColor
        if r >= 1: 
            dfs(image, r - 1, c, color, newColor)
        if c >= 1: 
            dfs(image, r, c - 1, color, newColor)
        if r + 1 < len(image):
            dfs(image, r + 1, c, color, newColor)
        if c + 1 < len(image[0]):
            dfs(image, r, c + 1, color, newColor)