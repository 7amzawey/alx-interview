#!/usr/bin/python3
"""Read a stdin line by line and computes metrics"""


import re
import sys


PATTERN = (
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \['
    r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] "GET /projects/260 HTTP/1\.1" '
    r'(200|301|400|401|403|404|405|500) \d+$'
)


def line_is_valid(line):
    return re.match(PATTERN, line) is not None


def print_stats(total_size, status_dict):
    print(f"File size: {total_size}")
    for key, value in sorted(status_dict.items()):
        print(f"{key}: {value}")


def main():
    total_size = 0
    status_dict = {}
    line_count = 0
    try:
        for line in sys.stdin:
            if line_is_valid(line) is False:
                pass
            parts = line.split(' ')
            total_size += int(parts[8])
            status = int(parts[7])
            if status in status_dict:
                status_dict[status] += 1
            else:
                status_dict[status] = 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_dict)

    except KeyboardInterrupt:
        print_stats(total_size, status_dict)


if __name__ == "__main__":
    main()
