#!/usr/bin/env python3
import sys
import signal
import re

"""
Regular expression to match the specified log format
"""
log_pattern = re.compile(r'(\S+) - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

"""
Initialize variables to keep track of total file size and status code counts
"""
total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """
    Prints the accumulated statistics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def process_line(line):
    """
    Processes a single line of log data.
    """
    global total_size, line_count

    """
    Use regex to match the expected format
    """
    match = log_pattern.match(line)
    if match:
        ip, status_code, file_size = match.groups()
        status_code = int(status_code)
        file_size = int(file_size)
        
        """
        Update total file size
        """
        total_size += file_size

        """
        Update the count for the status code if it's in the list of valid codes
        """
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

def handle_interrupt(signal, frame):
    """
    Handles keyboard interrupt (CTRL + C) by printing the statistics and exiting.
    """
    print_statistics()
    sys.exit(0)

"""
Set up signal handling for keyboard interrupt (CTRL + C)
"""
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        """
        Process the line
        """
        process_line(line.strip())

        """
        Every 10 lines, print statistics
        """
        if line_count > 0 and line_count % 10 == 0:
            print_statistics()
except Exception as e:
    print(f"Error: {e}")
finally:
    """
    In case the input ends without an interrupt, print the final statistics
    """
    print_statistics()
