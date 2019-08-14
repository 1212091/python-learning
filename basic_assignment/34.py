class NumberException(Exception):
    def __init__(self, message):
        super(NumberException, self).__init__(message)


input_value = input()

if int(input_value) == 0:
    raise NumberException("Cannot input 0 value")
