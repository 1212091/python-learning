class Person:
    name = "Carson"

    def __init__(self, name):
        self.name = name


print("Name of person: " + Person.name)
person = Person("Green")
print("Name of person: " + person.name)
