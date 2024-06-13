#!/usr/bin/python3
"""
Function to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island.

    :param grid: List of list of integers where 0 represents
    water and 1 represents land
    :return: Integer representing the perimeter of the island
    """


    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell starts with a perimeter contribution of 4
                perimeter += 4

                # Check upper cell
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2

                # Check left cell
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
