class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print(f"Hi, I am {self.name}")

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def info(self):
        super().say_hello()
        print(f"My salary is ${self.salary}.")

e1 = Employee("Oleg", 120)
e1.info()
