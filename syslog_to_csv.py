import re
import csv

# Read syslog data from a file
with open('target_host/syslog_from_target_host', 'r') as file:
    syslog_data = file.read()

# Define a regular expression pattern based on your syslog format
# Modify the pattern to match your syslog's timestamp and message format
pattern = r'^(\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}).+?(\b\w+\b\Z)'

# Parse syslog data and transform it to CSV format
csv_data = []
for line in syslog_data.split('\n'):
    match = re.match(pattern, line)
    if match:
        csv_data.append([match.group(1), match.group(2)])

# Write CSV data to a file
with open('syslog.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Date', 'Message'])  # CSV header
    csvwriter.writerows(csv_data)
