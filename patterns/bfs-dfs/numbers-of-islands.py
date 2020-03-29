import collections

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
  Input:
    11110
    11010
    11000
    00000
  Output: 1


Example 2:
  Input:
    11000
    11000
    00100
    00011
  Output: 3

"""


def numbersOfIslands(grid):
    count = 0
    for col_index, row_data in enumerate(grid):
        for row_index, cell_data in enumerate(row_data):
            if cell_data == 1:
                count += 1
                dfs(col_index, row_index, grid)
    return count


def dfs(x, y, grid):
    x_length, y_length = len(grid), len(grid[0])
    if x < 0 or x >= x_length or y < 0 or y >= y_length or grid[x][y] == 0:
        return
    grid[x][y] = 0
    dfs(x-1, y, grid)  # left
    dfs(x, y+1, grid)  # up
    dfs(x+1, y, grid)  # right
    dfs(x, y+1, grid)  # down


print(numbersOfIslands([
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]) == 1)


print(numbersOfIslands([
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]) == 3)
