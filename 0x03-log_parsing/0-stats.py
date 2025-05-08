#!/usr/bin/python3
import sys
import re

def print_stats(total_size, status_counts):
    """Print the statistics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def main():
    total_size = 0
    status_counts = {
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
            # Parse the line using regex
            match = re.match(
                r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$',
                line.strip()
            )
            if not match:
                continue  # Skip lines that don't match the format

            status_code = int(match.group(1))
            file_size = int(match.group(2))

            # Update metrics
            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Print stats on keyboard interrupt
        print_stats(total_size, status_counts)
        raise

    # Print final stats if there's no keyboard interrupt
    print_stats(total_size, status_counts)
