#!/usr/bin/python3
"""N Queens problem solver"""

import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, col, N):
    """
    Recursive function to solve N Queens problem
    """
    # Base case: If all queens are placed
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution then remove queen from board[i][col]
            board[i][col] = 0

    # If the queen can't be placed in any row in this column col then return False
    return False

def print_solution(board):
    """
    Print the solution
    """
    N = len(board)
    for i in range(N):
        for j in range(N):
            print("[{}, {}]".format(i, j), end=" ") if board[i][j] == 1 else print("_", end=" ")
        print()

def main():
    """
    Main function
    """
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Parse the argument as integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chess board
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N Queens problem
    if not solve(board, 0, N):
        print("No solution found")
        sys.exit(1)

    # Print the solution
    print_solution(board)

if __name__ == "__main__":
    main()

