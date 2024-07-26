class Employee:
    first_name = "Akbar"
    last_name = "Nurbekov"
    age = 17
    gender = "Mужчина"

    def get_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)
        print(self.gender)
        print()

    def set_first_name(self,first_name):
        self.first_name = first_name

    def set_last_name(self,last_name):
        self.first_name = last_name

    def set_age(self,age):
        self.age = age

    def set_gender(self,gender):
        self.gender = gender


emp1 = Employee()
emp2 = Employee()

emp1.get_info()
emp1.set_first_name(first_name="Azat")
emp1.get_info()


#метотдору жана свойстволору болот


