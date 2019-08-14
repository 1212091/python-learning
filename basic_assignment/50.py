from datetime import datetime, timedelta

input_data = raw_input()

datetime_object = datetime.strptime(str(input_data), '%H:%M:%S.%f') + timedelta(seconds=5)

print(str(datetime_object))
