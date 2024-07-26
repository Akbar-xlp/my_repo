class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class WorKingStudent(Employee, Student):
    def __init__(self, name, age, salary):
        Employee.__init__(self, name, salary)
        Student.__init__(self, name, age)


worKingStudent = WorKingStudent("Akbar", 17, 1000000)
worKingStudent.display()
print(WorKingStudent.__mro__)
print(WorKingStudent.mro())
