class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return self.radius ** 2 * 3.14


circle = Circle(2)
print("Area of circuit: " + str(circle.compute_area()))
