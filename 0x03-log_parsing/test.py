#!/usr/bin/python3
"""Read a stdin line by line and computes metrics."""


import sys


def print_stats(total_size, status_dict):
    """Print the stats of the file."""
    print(f"File size: {total_size}")
    for key, value in sorted(status_dict.items()):
        print(f"{key}: {value}")


def main():
    """Print out the metrics."""
    total_size = 0
    status_dict = {}
    line_count = 0
    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split(' ')
            total_size += int(parts[8])
            status = int(parts[7])

            if status in status_dict:
                status_dict[status] += 1
            else:
                status_dict[status] = 1

            line_count += 1

            if line_count == 10:
                print_stats(total_size, status_dict)
                line_count = 0
                total_size = 0
                status_dict = {}

    except KeyboardInterrupt:
        print_stats(total_size, status_dict)


if __name__ == "__main__":
    main()
