from datetime import datetime

input_unix_time = input()

ts = int(input_unix_time)

print(datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
