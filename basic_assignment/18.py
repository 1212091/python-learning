import re

input_data = raw_input()

raw_password_list = input_data.split(",")


def is_valid_password(password):
    return bool(re.match('^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$@#])', password)) and 6 < len(password) < 12


valid_password_list = filter(is_valid_password, raw_password_list)
print(valid_password_list)
