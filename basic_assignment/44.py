class Parentheses:
    open_list = ['{', '[', '(']
    close_list = ['}', ']', ')']

    def __init__(self, input_string):
        self.input_string = input_string

    def check_valid_parentheses(self):
        stack = []
        for letter in self.input_string:
            if letter in Parentheses.open_list:
                stack.append(letter)
            elif letter in Parentheses.close_list:
                if len(stack) > 0 and Parentheses.open_list[Parentheses.close_list.index(letter)] == \
                        stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False


parentheses = Parentheses("({[)]")
print(parentheses.check_valid_parentheses())
