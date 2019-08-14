num_iter = input(">")


class Number:
    def __init__(self):
        self.i = 0

    def y_range(self, n):
        while self.i < n:
            print("Value: " + str(self.i))
            yield self.i
            self.i += 7


iterator = Number()
generator = iterator.y_range(num_iter)

next(generator)
next(generator)
next(generator)
