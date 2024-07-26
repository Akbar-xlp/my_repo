class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Employee(Person):
    def __init__(self, name, work):
        super().__init__(name)
        self.__work = work

    @property
    def work(self):
        return self.__work


employee_1 = Employee("Akbar", "IT")
print(employee_1.name)
print(employee_1.work)
person_1 = Person("Josh")
print(person_1.name)
