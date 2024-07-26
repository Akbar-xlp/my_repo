"""
Dog деген класс жазыныздар
Анын name, age деген свойстволары жана
sleep, eat деген методдору болсун

Объект создание кылып ал обиектин
sleep деген методун чакырганда бизге '<name> the dog is sleeping'
деп чыгыш керек.
эгер eat методдун чакырсак анда '<name> the dog is eating'
деп чыгыш керек
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print()
        print(f"{self.name} the dog is eating.")
        print()

    def sleep(self):
        print()
        print(f"{self.name} the dog is sleeping.")
        print()


my_dog = Dog("Шарик", 5)
my_dog.sleep()
my_dog.eat()
