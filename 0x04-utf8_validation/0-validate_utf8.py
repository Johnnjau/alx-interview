#!/usr/bin/python3
"""
determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding.
    """
    bytes_num = 0  # num of bytes for the current char

    for byte in data:
        # isolate LSB
        current_byte = byte & 0xff
        if bytes_num == 0:
            # if we are processing 1st byte
            if current_byte < 0x80:
                bytes_num = 1  # 1-byte ASCII char
            elif current_byte & 0b11100000 == 0b11000000:
                bytes_num = 2
            elif current_byte & 0b11110000 == 0b11100000:
                bytes_num = 3
            elif current_byte & 0b11111000 == 0b11110000:
                bytes_num = 4
            else:
                return False
        else:
            if current_byte & 0b11000000 != 0b10000000:
                return False
        bytes_num -= 1

    return bytes_num == 0
