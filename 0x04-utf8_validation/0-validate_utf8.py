#!/usr/bin/python3
""" This is a method that determines if a given data set represents a valid
UTF-8 encoding"""


def validUTF8(data):
    """Number of bytes in the current UTF-8 character"""
    number_of_bytes = 0

    # Iterates through each integer in the data list
    for byte in data:
        # If the current byte is the start of a new character
        if number_of_bytes == 0:
            # Dettermines the number of bytes required for the character
            if byte >> 5 == 0b110:
                number_of_bytes = 1
            elif byte >> 4 == 0b1110:
                number_of_bytes = 2
            elif byte >> 3 == 0b11110:
                number_of_bytes = 3
            # If the current byte starts with 0, it's a single-byte character
            elif byte >> 7 == 0b0:
                continue
            else:
                return False
        else:
            # Checks if the current byte is a continuation byte
            if byte >> 6 != 0b10:
                return False
            number_of_bytes -= 1

    # If there are remaining bytes required, the data is invalid then
    return number_of_bytes == 0
