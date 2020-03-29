import collections

"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.

https://leetcode.com/problems/rotting-oranges/
"""


def rottingOranges(grid):
    count = 0
    rotten = collections.deque()
    for irow, row_data in enumerate(grid):
        for icol, cell_data in enumerate(row_data):
            if cell_data == 2:
                rotten.append((irow, icol, 0))

    row_length, col_length = len(grid), len(grid[0])
    while rotten:
        irow, icol, count = rotten.popleft()
        for x, y in ((irow-1, icol), (irow, icol-1), (irow + 1, icol), (irow, icol + 1)):
            if 0 <= x < row_length and 0 <= y < col_length:
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    rotten.append((x, y, count+1))
    if any(1 in row for row in grid):
        return -1
    return count


print(rottingOranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4)
print(rottingOranges([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1)
print(rottingOranges([[0, 2]]) == 0)
