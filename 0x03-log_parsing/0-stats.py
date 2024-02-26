#!/usr/bin/python3
import sys
import signal

# Function to handle keyboard interruption
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Function to print statistics
def print_statistics():
    print(f"Total file size: File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

# Initialize variables
total_size = 0
status_codes = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        # Check if the line has the correct format
        if len(parts) == 7 and parts[5].isdigit() and parts[6].isdigit():
            status_code = parts[5]
            file_size = int(parts[6])
            # Update total file size and status code count
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            line_count += 1
            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_statistics()
except KeyboardInterrupt:
    # Handle any keyboard interruption
    print_statistics()
