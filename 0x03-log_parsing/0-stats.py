#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys
import re

def print_stats(status_codes, total_size):
    """Prints the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def main():
    total_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            match = re.match(
                r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$', 
                line.strip()
            )
            if not match:
                continue

            status = int(match.group(1))
            file_size = int(match.group(2))

            total_size += file_size
            if status in status_codes:
                status_codes[status] += 1

            if line_count % 10 == 0:
                print_stats(status_codes, total_size)

    except KeyboardInterrupt:
        print_stats(status_codes, total_size)
        raise

    print_stats(status_codes, total_size)

if __name__ == "__main__":
    main()
