class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = self.name + "s age is " + str(self.age)