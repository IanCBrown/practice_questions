#!/bin/python3

import math
import os
import random
import re
import sys

# Hackerrank DFS, Connected Cells 
# Completed along with video lesson from Hackerrank
def getRegionSize(grid, row, column):
    if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[row]):
        return 0
    if grid[row][column] == 0:
        return 0
    
    grid[row][column] = 0 
    size = 1

    # in range row - 1 to row + 1
    # use row + 2, bc range is exclusive 
    for r in range(row - 1, row + 2):
        for c in range(column - 1, column + 2):
            if r != row or c != column:
                size += getRegionSize(grid, r, c)
    return size


def maxRegion(grid):
    max_region = 0 
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                size = getRegionSize(grid, row, col) 
                max_region = max(size, max_region)
    
    return max_region