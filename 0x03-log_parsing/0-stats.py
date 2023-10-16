import sys

status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        if line_count % 10 == 0:
            print("Total file size: File size:", total_file_size)
            for code, count in sorted(status_code_count.items()):
                if count > 0:
                    print(f"{code}: {count}")

        parts = line.split()
        if len(parts) < 7:
            continue

        status_code = parts[-2]
        try:
            status_code = int(status_code)
        except ValueError:
            continue

        if status_code in status_code_count:
            status_code_count[status_code] += 1

        file_size = parts[-1]
        try:
            file_size = int(file_size)
            total_file_size += file_size
        except ValueError:
            continue

except KeyboardInterrupt:
    print("Total file size: File size:", total_file_size)
    for code, count in sorted(status_code_count.items()):
        if count > 0:
            print(f"{code}: {count}")
