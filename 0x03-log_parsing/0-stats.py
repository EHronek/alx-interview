#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys
import re


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
    for key in sorted(dict_status_codes.keys()):
        if dict_status_codes[key] != 0:
            print("{}: {}".format(key, dict_status_codes[key]))


t_file_size = 0
counter = 0
dict_status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    for line in sys.stdin:
        # Use regex to properly parse the line
        match = re.match(
            r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$',
            line.strip()
        )
        if not match:
            continue  # Skip invalid lines

        status_code = int(match.group(1))
        file_size = int(match.group(2))

        # Update metrics
        t_file_size += file_size
        if status_code in dict_status_codes:
            dict_status_codes[status_code] += 1

        counter += 1

        # Print every 10 lines
        if counter % 10 == 0:
            print_stats(dict_status_codes, t_file_size)

except KeyboardInterrupt:
    # Print stats on CTRL+C
    print_stats(dict_status_codes, t_file_size)
    raise

# Print final stats if we reach end of input
print_stats(dict_status_codes, t_file_size)