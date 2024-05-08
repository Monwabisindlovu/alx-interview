#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Checks if a list of integers represents a valid UTF-8 encoding."""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Iterate through each integer in the data
    for num in data:
        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Count the number of bytes for this character
            if num >> 7 == 0b0:
                num_bytes = 1
            elif num >> 5 == 0b110:
                num_bytes = 2
            elif num >> 4 == 0b1110:
                num_bytes = 3
            elif num >> 3 == 0b11110:
                num_bytes = 4
            else:
                return False

            # For a single byte character
            if num_bytes == 1:
                continue
        else:
            # Check if the current integer is a valid continuation byte
            if num >> 6 != 0b10:
                return False

        # Decrement the number of remaining bytes
        num_bytes -= 1

    # If there are remaining bytes at the end of the data, it's invalid
    return num_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))

