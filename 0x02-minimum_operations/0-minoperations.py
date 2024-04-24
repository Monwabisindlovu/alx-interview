#!/usr/bin/python3
"""
Calculates the minimum number of operations needed to achieve n
characters
using only Copy All and Paste operations.
"""

def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve n
    characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations needed.
    """
    if n <= 1:
        return 0

    # Initialize an array to store the minimum operations for each number up to n
    dp = [0] * (n + 1)

    # Iterate from 2 to n
    for i in range(2, n + 1):
        # Initialize the minimum operations for current number as infinity
        dp[i] = float('inf')
        # Iterate from 1 to i // 2 (as beyond that it's not possible to achieve)
        for j in range(1, i // 2 + 1):
            # If j is a divisor of i
            if i % j == 0:
                # Calculate the number of operations needed for i by copying j times
                # and pasting (i // j - 1) times
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]

# Example usage:
if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n,
        minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n,
        minOperations(n)))
