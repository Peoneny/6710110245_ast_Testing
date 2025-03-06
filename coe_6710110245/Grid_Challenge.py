import math
import os
import random
import re
import sys

def gridChallenge(grid):
    sorted_grid = ["".join(sorted(row)) for row in grid]
    n = len(sorted_grid)
    m = len(sorted_grid[0])
    
    for col in range(m):
        for row in range(n - 1):
            if sorted_grid[row][col] > sorted_grid[row + 1][col]:
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
