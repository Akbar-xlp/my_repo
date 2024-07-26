# class Person:
#     def __init__(self,first_name, last_name, email, password="user_password"):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.password = password
#
#     def get_info(self):
#         print(
#             self.first_name,
#             self.last_name,
#             self.email,
#             self.password
#         )
#     def change_password(self, password):
#         self.password = password
#
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __del__(self, ):
#         print("Finished")
#
# ob_1 = Person("Akbar", "Nurbekov", "akbar@gmail.com", "akbar_password")
# ob_1.get_info()
# full_name = ob_1.get_full_name()
# print(full_name)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age < 18:
#             print("Sorry, the age cannot be negative")
#         else:
#             self._age
#
# person_1 = Person("Akbar", 19)
# print(person_1.age)
# person_1.age = 17
# print(person_1.age,)

class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if color in ["black", "white", "pink", "yellow", "red"]:
            self.__color = color
        else:
            print("Sorry, the color must be black,white,pink,yellow,red")
            print(f"The dog color can't be {color}")


dog_1 = Dog("sharik",3, "black")
print(dog_1.color)
dog_1.color = "brown"
