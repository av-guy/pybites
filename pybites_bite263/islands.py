def discover(grid, row, column):
    mark_islands(row, column, grid)
    # look up
    if row - 1 >= 0:
        if grid[row - 1][column] == 1:
            discover(grid, row - 1, column)
    # look left
    if column - 1 >= 0:
        if grid[row][column - 1] == 1:
            discover(grid, row, column - 1)
    # look right
    if column + 1 < len(grid[row]):
        if grid[row][column + 1] == 1:
            discover(grid, row, column + 1)
    # look down
    if row + 1 < len(grid):
        if grid[row + 1][column] == 1:
            discover(grid, row + 1, column)

def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    # islands = 0         # var. for the counts
    # .....some operations.....
    # mark_islands(r, c, grid)
    # return islands
    islands = 0
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column == 1:
                islands += 1
                discover(grid, i, j)
    return islands


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    grid[i][j] = '#'