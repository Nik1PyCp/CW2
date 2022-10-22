class Base:
    def __init__(self):
        self.height = 185
class NoBase:
    def __init__(self):
        self.width = 100
    def method(self):
        print(123)

class Child(Base, NoBase):
    def print(self):
        print(self.height)
        self.method()

child1 = Child()
child1.print()
