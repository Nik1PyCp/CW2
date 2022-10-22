class Student:
    def __init__(self, name="No name", surname="No surname", age="No age", height="No height", hobby="No hobby"):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.hobby = hobby

class Group:
    def __init__(self, namme):
        self.namme = namme
        self.student = []

    def add_students(self, studentname):
        self.student.append(studentname)



    def print_student_names(self):
        if self.student != []:
            print(f"Names and surnames of {self.namme} group:")
            for student in self.student:
                 print(f"{student.name} {student.surname} {student.age} {student.height} {student.hobby} ")
        else:
            print(f"There are not student in {self.namme}!")




g1 = Group("FI89")

g1.add_students(Student("Oleg", "Bobyl", 15, 170, "football"))
g1.add_students(Student("OLga", "Koval", 20, 169,  "art"))
g1.add_students(Student("Igor", "Bobko", 19, 175))


g1.print_student_names()
