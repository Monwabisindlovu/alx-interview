#!/usr/bin/python3
"""0-stats.py

Reads stdin line by line and computes metrics based on the input format:
    <status code> <file size>
Prints the total file size and counts of possible status codes in the format:
    File size: <total size>
    <status code>: <number>
"""

import fileinput


def print_logs(file_size: int, status_codes: dict):
    """Prints file size and status code counts.

    Args:
        file_size (int): Total file size.
        status_codes (dict): Dictionary of status codes and their counts.

    Returns:
        None
    """
    print("File size:", file_size)
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


def parse_log():
    """Parses logs from stdin and computes metrics."""
    file_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    current_line = 0

    try:
        for line in fileinput.input():
            data = line.split()
            if len(data) < 2:
                continue
            file_size += int(data[-1])
            status = data[-2]
            if status in status_codes:
                status_codes[status] += 1
            current_line += 1
            if current_line % 10 == 0:
                print_logs(file_size, status_codes)
    except KeyboardInterrupt:
        pass
    print_logs(file_size, status_codes)


if __name__ == "__main__":
    parse_log()
