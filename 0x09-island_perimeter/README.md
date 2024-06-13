# Island Perimeter

This project implements a function to calculate the perimeter of an island in a grid. The grid is represented as a list of lists of integers, where `0` represents water and `1` represents land.

## Requirements

- The project will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- Code should follow the PEP 8 style guide (version 1.7).
- No additional modules should be imported.
- All modules and functions must be documented.
- All files must be executable.

## Function Description

### island_perimeter

The function `island_perimeter(grid)` calculates the perimeter of the island described in `grid`.

- **Parameters:**
  - `grid` (list of list of int): The grid representing the map where `0` represents water and `1` represents land.

- **Returns:**
  - `int`: The perimeter of the island.

### Example

Here's an example of how to use the function:

```python
#!/usr/bin/python3
"""
Example usage of island_perimeter function.
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output should be 12
