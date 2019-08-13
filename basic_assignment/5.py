class Printer:
    def __init__(self):
        self.input_data = raw_input(">")

    def get_string(self):
        print("Input: " + str(self.input_data))

    def print_string(self):
        print("Upper case result: " + str(self.input_data).upper())


a = Printer()
a.get_string()
a.print_string()
