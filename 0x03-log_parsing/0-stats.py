#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


def print_stats(dict_status_codes, t_file_size):
    """
    Method to print
    Args:
        dict_status_codes: dict of status codes
        t_file_size: total of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(t_file_size))
    for key, value in sorted(dict_status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


t_file_size = 0
code = 0
counter = 0
dict_status_codes = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        # trimming
        parsed_line = line.split()
        # inverting
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                # file size
                t_file_size += int(parsed_line[0])
                # status code
                code = parsed_line[1]

                if (code in dict_status_codes.keys()):
                    dict_status_codes[code] += 1

            if (counter == 10):
                print_stats(dict_status_codes, t_file_size)
                counter = 0

finally:
    print_stats(dict_status_codes, t_file_size)
