#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'canPlaceSecurityCameras' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER N
#  2. 2D_INTEGER_ARRAY grid
#

def canPlaceSecurityCameras(N, grid):
    if N == 0:
        return 1
    if N > min(len(grid), len(grid[0])):
        return 0
    if N > sum(row.count(0) for row in grid):
        return 0
    
    cols = set()
    diagonals = set()
    anti_diagonals = set()
    
    def backtrack(row):
        if row == N:
            return 1
        
        
        for col in range(N):
            if grid[row][col] == 1:
                continue
            if col in cols or (row-col) in diagonals or (row+col) in anti_diagonals:
                continue
                
            cols.add(col)
            diagonals.add(row-col)
            anti_diagonals.add(row+col)
            
            if backtrack(row + 1):
                return 1
            
            cols.remove(col)
            diagonals.remove(row-col)
            anti_diagonals.remove(row+col)
        
        return 0
    
    return backtrack(0)


if __name__ == '__main__':
    N = int(input().strip())

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = canPlaceSecurityCameras(N, grid)

    print(int(result))
