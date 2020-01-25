grid = [[1,2,3],[4,0,5],[6,7,8]]

def neighbors(grid, row, col, n):
    neighbors = []
    vals = []
    if n == 4:
        # four_directional
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
    elif n == 8:
        # eight_directional 
        neighbors = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
    else:
        return

    for neighbor in neighbors:
        r = (row + neighbor[0])
        c = (col + neighbor[1])

        if (r < len(grid) and r >= 0) and (c < len(grid[0]) and c >= 0):
            vals.append(grid[r][c])
    
    return vals


print(neighbors(grid, 1, 1, 4))
print(neighbors(grid, 1, 1, 8))
