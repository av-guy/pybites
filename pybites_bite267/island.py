# Hint:
# You can define a helper funtion: get_others(map, row, col) to assist you.
# Then in the main island_size function just call it when traversing the map.


def look_around(grid, row, column):
    perimeter = 0
    if row - 1 >= 0:
        if grid[row - 1][column] == 0:
            perimeter += 1
    else:
        perimeter += 1
    if column - 1 >= 0:
        if grid[row][column - 1] == 0:
            perimeter += 1
    else:
        perimeter += 1
    if column + 1 < len(grid[row]):
        if grid[row][column + 1] == 0:
            perimeter += 1
    else:
        perimeter += 1
    if row + 1 < len(grid):
        if grid[row + 1][column] == 0:
            perimeter += 1
    else:
        perimeter += 1
    return perimeter


def island_size(grid):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    for i, row in enumerate(grid):
        for j, column in enumerate(row):
            if column == 1:
                print('found a 1')
                perimeter += look_around(grid, i, j)
                print(perimeter, 'is perimeter for', i, j)
    return perimeter
