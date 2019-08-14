class American:
    @staticmethod
    def print_nationality():
        print("I am American")

    def hello(self):
        print("Hello I am American people")


class NewYorker(American):
    def hello(self):
        print("Hello I am new yorker")


american = American()
american.hello()

new_yorker = NewYorker()
new_yorker.hello()
