# 0x02. Minimum Operations

This project aims to solve the "Minimum Operations" problem, which involves calculating the minimum number of operations needed to achieve a given number of characters in a text file using only "Copy All" and "Paste" operations.

## Problem Description

In a text file, there is a single character `H`. The text editor can execute only two operations: Copy All and Paste. Given a number `n`, the task is to write a method that calculates the fewest number of operations needed to result in exactly `n H` characters in the file.

### Example:

Given `n = 9`, the operations would be as follows:
- H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
Number of operations: 6

## Implementation

The solution provided employs dynamic programming to efficiently calculate the minimum number of operations required. The `minOperations` function in `0-minoperations.py` accomplishes this task.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder of the project is mandatory
- Code documentation is required
- Code should adhere to PEP 8 style (version 1.7.x)
- All files must be executable

## Usage

To test the implementation, execute `0-main.py`. You can modify this file to test different values of `n`.

```bash
./0-main.py
Additional Resources
Dynamic Programming (GeeksforGeeks)
Prime Factorization (Khan Academy)
How to optimize Python code
Greedy Algorithms (GeeksforGeeks)
Mock Technical Interview
For further practice, consider engaging in a mock technical interview.

Author
This solution was authored by [Monwabisi Ndlovu].
