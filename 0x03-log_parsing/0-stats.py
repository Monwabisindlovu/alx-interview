#!/usr/bin/python3

import sys
import signal
import re

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
count = 0

def signal_handler(sig, frame):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    count += 1
    match = re.match(r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$", line)
    if match:
        ip, date, status_code, file_size = match.groups()
        total_size += int(file_size)
        status_codes[int(status_code)] += 1
    if count == 10:
        print(f"File size: {total_size}")
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f"{code}: {status_codes[code]}")
        count = 0
