import abc
from math import pi


class ISape(abc.ABC):
    @abc.abstractmethod
    def area(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def perimeter(self, *args, **kwargs):
        print("Perimetr")


class Circle(ISape):
    def area(self, *args, **kwargs):
        return pi * kwargs["radius"] ** 2

    def perimeter(self, *args, **kwargs):
        return 2 * pi * kwargs["radius"]


class Rectangle(ISape):
    def area(self, *args, **kwargs):
        return kwargs["width"] * kwargs['height']

    def perimeter(self, *args, **kwargs):
        return 2 * (kwargs["width"] + kwargs['height'])


circle = Circle()
print(circle.area(radius=5))
print(circle.perimeter(radius=5))
rect = Rectangle()
print(rect.area(width=2, height=3))
print(rect.perimeter(width=2, height=3))
