# 0x07. Rotate 2D Matrix

## Description

This project involves implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. The task requires a good understanding of matrix manipulation and in-place operations in Python.

## Concepts

- **Matrix Representation in Python**: Understanding how 2D matrices are represented using lists of lists in Python.
- **In-place Operations**: Performing operations on data without creating a copy of the data structure.
- **Matrix Transposition**: Swapping rows and columns of the matrix.
- **Reversing Rows in a Matrix**: Reversing the order of elements in each row.

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the folder of the project is mandatory.
- Code should use the pycodestyle style (version 2.8.0).
- No imports of any module are allowed.
- All modules and functions must be documented.
- All files must be executable.

## Files

- `0-rotate_2d_matrix.py`: Contains the function to rotate the matrix.
- `main_0.py`: Test script to verify the function.

## Usage

1. **Rotate 2D Matrix Function**: `0-rotate_2d_matrix.py`

    ```python
    #!/usr/bin/python3
    """
    Rotate 2D Matrix
    """

    def rotate_2d_matrix(matrix):
        """
        Rotate the given n x n 2D matrix 90 degrees clockwise in place.
        Args:
            matrix (list of list of int): The n x n matrix to rotate.
        """
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()
    ```

2. **Test Script**: `main_0.py`

    ```python
    #!/usr/bin/python3
    """
    Test 0x07 - Rotate 2D Matrix
    """
    rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

    if __name__ == "__main__":
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        rotate_2d_matrix(matrix)

        # Print each row on a new line
        for row in matrix:
            print(row)
    ```

3. **Execution**

    - Make the test script executable:
        ```sh
        chmod u+x main_0.py
        ```
    - Run the test script:
        ```sh
        ./main_0.py
        ```

    - Expected output:
        ```sh
        [7, 4, 1]
        [8, 5, 2]
        [9, 6, 3]
        ```

## Author

- Monwabisi Ndlovu
-monwabisindlovu78@gmail.com

