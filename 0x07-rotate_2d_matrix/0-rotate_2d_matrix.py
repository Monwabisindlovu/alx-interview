#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    n = len(matrix)  # Assuming the matrix is square (n x n)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

# Example usage
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
