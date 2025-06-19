#!/usr/bin/python3
"""the islands Perimeter problem"""


def island_perimeter(grid):
    """Calcualates the perimeter of the island in grid"""
    per = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    per += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    per += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    per += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    per += 1
    return per
