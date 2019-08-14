__metaclass__ = type


class Shape:
    def __init__(self):
        pass

    def compute_area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        super(Square, self).__init__()
        self.length = length

    def compute_area(self):
        return self.length ** 2


square = Square(10)
print("Area of square: " + str(square.compute_area()))
