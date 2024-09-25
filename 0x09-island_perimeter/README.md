###Island Perimeter Problem

###Overview
This Python module provides a function called island_perimeter that calculates the perimeter of an island represented in a 2D grid. The grid consists of integers, where 1 represents land and 0 represents water.

###Function
island_perimeter(grid)
Parameters:

grid (List[List[int]]): A 2D list of integers containing 0 (water) or 1 (land).
Returns:

int: The perimeter of the island.
Description
The island_perimeter function iterates through the provided grid and calculates the perimeter of the island(s) represented in it. The perimeter is determined by checking the adjacent cells of each land cell (1) in the grid:

If a neighboring cell is out of bounds or contains water (0), it contributes to the perimeter count.

###Code Explanation
Function Definition:

python code
def island_perimeter(grid):
Variable Initialization:

python code
p = 0
A variable p is initialized to accumulate the perimeter count.

###Nested Loop to Traverse the Grid:

python code
for i in range(len(grid)):
    for j in range(len(grid[i])):
The outer loop iterates over each row, and the inner loop iterates over each column of the current row.

Check for Land Cells:

###python code
if (grid[i][j] == 1):
The function checks if the current cell is land.

Calculate Perimeter Contribution:

Each adjacent cell (up, down, left, right) is checked:

###python code
if (i <= 0 or grid[i - 1][j] == 0): p += 1
if (i >= len(grid) - 1 or grid[i + 1][j] == 0): p += 1
if (j <= 0 or grid[i][j - 1] == 0): p += 1
if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0): p += 1
Each valid contribution to the perimeter increments p.

Return the Calculated Perimeter:

###python code
return p
The function returns the total perimeter of the island.

Example Usage
python
Copy code
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
perimeter = island_perimeter(grid)
print(perimeter)  # Output: 8
